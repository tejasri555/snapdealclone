

from snapdealapp.views import redirect
from snapdealapp.models import *
from django.shortcuts import render



def SearchCategoryView(request,string):
    if string is not None:
        x = list(Category.objects.filter(title__icontains=string))
        if x ==[]:
            x = list(Category.objects.all())
            return render(request, 'searchcategoryfail.html', {'category': x})
        return render(request, 'searchcategory.html', {'category': x})

def SearchProductView(request,string):
    string = " ".join(string.split('-'))

    product=None
    if string is not None:
        product = list(
            Product.objects.values('category__id', 'id', 'title', 'image', 'price',
                                       'description').filter(title__icontains=string))
        if product!=[]:
            return render(request, 'productSearchResults.html', {'product': product})
        if product == []:
            product = list(Category.objects.values('id', 'product__id', 'product__title', 'product__image', 'product__description',
                                            'product__price', 'product__rating').filter(title__icontains=string))
            if product==[]:
                product = list(
                    Category.objects.values('id', 'product__id', 'product__title', 'product__image', 'product__description',
                                            'product__price', 'product__rating'))
                return render(request, 'search_failure.html', {'product': product})
        else:
            return render(request, 'seach_cat.html', {'product': product})

        return render(request, 'productSearchResults.html', {'product': product})

    return render(request, 'productSearchResults.html')

def search_all(request,**kwargs):

    method_dict = dict(request.GET)
    if (method_dict['q'][0] == ''):
        str='xxx'
    else:
        str='-'.join(list(method_dict['q'][0].split()))

    if (method_dict['r']) == ['category']:
        return redirect('snapdealapp:list_category',str)
    elif (method_dict['r']) == ['product']:
        return redirect('snapdealapp:list_product',str)