from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView,DeleteView
from django.contrib.auth.mixins import *
from snapdealapp.models import *
class Orderlistview(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = OrderedItems
    context_object_name = 'order'
    template_name = "order.html"
    def get_queryset(self):
        user = self.request.user
        return OrderedItems.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        c = list(OrderedItems.objects.values().filter(user_id=self.request.user.id))

        price=0
        for i in c:
            product_id = i['products_id']
            product = Product.objects.get(id=product_id)
            price += product.price

        context = super(Orderlistview, self).get_context_data(**kwargs)
        context.update({'user_permissions': self.request.user.get_all_permissions()})
        context.update({'total': price})

        return context


@login_required
def order(request,**kwargs):
    return redirect('snapdealapp:order_html')

@login_required
def place_order(request,**kwargs):

    price=0
    try:
        c=list(Cart.objects.values().filter(user_id=request.user.id))
        for i in c:
            product_id = i['products_id']
            product = Product.objects.get(id=product_id)
            price+=product.price
            order= OrderedItems(user=request.user, products=product, subtotal=product.price, image=product.image, quantity=1)
            order.save()
            car = Cart.objects.get(id=i['id'])
            car.delete()

        return redirect('snapdealapp:order_html')

    except:
        pass
        return redirect('snapdealapp:order_html')

class DeleteOrderedlistView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = OrderedItems
    template_name = 'deleteform.html'
    success_url = reverse_lazy('snapdealapp:order_html')

    def has_permission(self):
        user_id = self.request.user.id
        check_user =OrderedItems.objects.get(pk=self.kwargs['pk']).user.id

        if not user_id == check_user:
            self.raise_exception = True
            success_url = reverse_lazy('snapdealapp:order_html')
            return False
        else:
            def get(self, request, *args, **kwargs):
                return self.post(request, args, kwargs)

            success_url = reverse_lazy('snapdealapp:order_html')
            return True
