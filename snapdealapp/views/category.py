
from django.views.generic import ListView, DetailView ,CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import *

from snapdealapp.models import *


class CategoryMainPage(ListView):
    login_url = '/login/'

    model = Category
    context_object_name='category'
    template_name = "category_main.html"

    def get_context_data(self,**kwargs):
        context=super(CategoryMainPage,self).get_context_data(**kwargs)
        product = list(
            Category.objects.values('id', 'product__id', 'product__title', 'product__image', 'product__description',
                                    'product__price', 'product__rating'))
        for i in product:
            if i['product__id'] is None:
                product = None

        context.update({
            'user_permissions': self.request.user.get_all_permissions(),
            'product': product,
        })
        return context


class AllProducts(ListView):
    login_url = '/login/'

    model = Product
    context_object_name='product'
    template_name = "productSearchResults.html"

    def get_context_data(self,**kwargs):
        context=super(AllProducts,self).get_context_data(**kwargs)
        return context
class CategoryListView(ListView):
    login_url = '/login/'

    model = Category
    context_object_name='category'
    template_name = "category.html"

    def get_context_data(self,**kwargs):
        context=super(CategoryListView,self).get_context_data(**kwargs)
        # import ipdb
        # ipdb.set_trace()
        # pass
        return context



class ProductList(ListView):
    login_url = '/login/'

    model = Product
    context_object_name = 'category'
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        # import ipdb
        # ipdb.set_trace()
        # pass
        return context


from django import forms
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude= ['id','active']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'enter title'  }),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }

from django.views.generic.edit import CreateView
class CreateCategoryView(CreateView):

    model=Category
    form_class = CategoryForm
    template_name = 'categoryForm.html'

    success_url=reverse_lazy('snapdealapp:category_html')




class UpdateCategoryView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categoryForm.html'
    success_url = reverse_lazy('snapdealapp:category_html')


class DeleteCategoryView(DeleteView):
    model=Category
    success_url = reverse_lazy('snapdealapp:category_html')
    def get(self,request,*args,**kwargs):
        return self.post(request,args,kwargs)