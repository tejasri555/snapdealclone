from django.core.serializers import json
from django.forms import forms
from django.http import HttpResponse
from django.views import View

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import *
from django.views.generic.detail import *
from django.views.generic import ListView, DetailView ,CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import *

from snapdealapp.models import *

class ProductList(DetailView):

    model = Category
    context_object_name = 'category_list'
    template_name = "product.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Category, **self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        category = context.get('category_list')

        context['categoryID'] = category.id

        print(type(category))
        product = list(
            Category.objects.values('id', 'product__id', 'product__title','product__image', 'product__description','product__price','product__rating').filter(
                id=category.id))
        for i in product:
            if i['product__id'] is None:
                product=None

        context.update({
            'user_permissions': self.request.user.get_all_permissions(),
            'product':product,
        })
        return context




class ProductDetails( DetailView):

    model = Product
    context_object_name = 'products'
    template_name = 'ProductList.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetails, self).get_context_data(**kwargs)
        product= context.get('products')
        # import ipdb
        # ipdb.set_trace()
        context.update({
            'user_permissions': self.request.user.get_all_permissions(),
            'product':product ,
        })
        return context


from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['id', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'units': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter units'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter rating'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }
from django.views.generic.edit import CreateView
class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'productForm.html'
    def get_context_data(self, **kwargs):

        context = super(CreateProductView, self).get_context_data(**kwargs)
        context.update({'product_form': context.get('form')})
        return context
    def post(self, request, *args, **kwargs):

        category = get_object_or_404(Category, pk=kwargs['pk'])
        product_form = ProductForm(request.POST,request.FILES)
        form_class = ProductForm

        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.category = category
            product.save()
        return redirect('snapdealapp:product_html', self.kwargs.get('pk'))


class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'productForm.html'
    def get_context_data(self, **kwargs):
        context = super(UpdateProductView, self).get_context_data(**kwargs)
        product_form = context.get('product')
        context.update({'product_form': context.get('form')})
        return context

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs.get('pk'))

        form = ProductForm(request.POST, instance=product)
        form.save()
        return redirect('snapdealapp:product_html',
                        self.kwargs.get('category_id'))


class DeleteProductView(DeleteView):
    # login_url = '/login/'
    # permission_required = 'onlineapp.college_list'
    # permission_denied_message = 'Sorry ! u cant add..login before u add'
    model=Product
    success_url = reverse_lazy('snapdealapp:category_html')
    def get(self, request, *args, **kwargs):
        return self.post(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        self.delete(request, args, kwargs)
        return redirect("snapdealapp:product_html", self.kwargs.get('category_id'))

