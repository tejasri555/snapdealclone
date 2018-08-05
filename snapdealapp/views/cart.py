

from  snapdealapp.models import *

from django.views.generic import DeleteView, ListView

from django.shortcuts import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class Cartlistview(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Cart
    context_object_name = 'cart'
    template_name = "cart.html"

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super(Cartlistview, self).get_context_data(**kwargs)
        context.update({'user_permissions': self.request.user.get_all_permissions()})
        return context



def add_to_cart(request,**kwargs):

    if request.user.is_authenticated:

        product_id = kwargs.get('pk')
        user = request.user
        product = Product.objects.get(id=product_id)
        try:
            cart=Cart.objects.get(user=user)
            if product in list(cart):
                pass
            else:
                itemtocart = Cart(user=user, products=product, subtotal=product.price, image=product.image, quantity=1)
                itemtocart.save()
                return redirect('snapdealapp:cart')

            return redirect('snapdealapp:cart')
        except:

            itemtocart = Cart(user=user, products=product, subtotal=product.price, image=product.image,quantity=1)
            itemtocart.save()
            return redirect('snapdealapp:cart')
    else:
        return redirect('snapdealapp:login_html')



class DeleteCartView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):

    model = Cart
    template_name = 'deleteform.html'
    success_url = reverse_lazy('snapdealapp:cart')

    def has_permission(self):
        user_id = self.request.user.id
        check_user = Cart.objects.get(pk=self.kwargs['pk']).user.id


        if not user_id == check_user:
            self.raise_exception = True
            success_url = reverse_lazy('snapdealapp:cart')
            return False
        else:
            def get(self, request, *args, **kwargs):
                return self.post(request, args, kwargs)

            success_url = reverse_lazy('snapdealapp:cart')
            return True



def clear_cart(request):
    price = 0
    import ipdb
    ipdb.set_trace()
    try:
        c = list(Cart.objects.values().filter(user_id=request.user.id))
        for i in c:
            product_id = i['products_id']
            product = Product.objects.get(id=product_id)
            price += product.price
            car = Cart.objects.get(id=i['id'])
            car.delete()

        return redirect('snapdealapp:cart')

    except:
        return redirect('snapdealapp:cart')


