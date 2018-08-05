from django import forms
from django.shortcuts import render
def payment_success(request):
    return render(request, 'payment_success.html')

class ProductForm(forms.ModelForm):
    class Meta:


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'units': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter units'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter rating'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter description'}),
        }
def payment_options(request):
    return render(request, 'payment_options.html')
