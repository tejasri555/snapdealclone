from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from  snapdealapp.models import Address

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django import forms
from django.shortcuts import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
class AddressListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model =Address
    context_object_name = 'address'
    template_name = "address.html"

    def get_context_data(self, **kwargs):
        context = super(AddressListView, self).get_context_data(**kwargs)
        user = self.request.user

        print(type(user))
        address = list(
            Address.objects.values('id', 'country', 'fullname','mobileno','pincode','city','street',
             'landmark','state' ,'address_type').filter(user_id=user.id))

        context.update({
            'user_permissions': self.request.user.get_all_permissions(),
            'address': address,
        })
        return context

class AddressForm(forms.ModelForm):
    mobileno = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mobileno'}),
                                help_text=(
                                    "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")),

    class Meta:
        model = Address
        exclude= ['id','user']

        # fields = ('country', 'fullname', 'pincode','street','mobileno','landmark','city','state','address_type' , )
        widgets={
            'country':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'enter title'  }),
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'mobileno':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'landmark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'address_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
        }
from django.views.generic.edit import CreateView
class CreateAddressView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Address
    form_class = AddressForm
    template_name = 'addressForm.html'

    def get_context_data(self, **kwargs):
        context = super(CreateAddressView, self).get_context_data(**kwargs)
        context.update({'address_form': context.get('form')})
        return context
    def post(self, request, *args, **kwargs):
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            address = address_form.save(commit=False)
            address.user = request.user
            address.save()
        return redirect('snapdealapp:address_html')

class UpdateAddressView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    model = Address
    form_class = AddressForm
    template_name = 'addressForm.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateAddressView, self).get_context_data(**kwargs)
        address_form = context.get('address')
        context.update({'address_form': context.get('form')})
        return context

    def post(self, request, *args, **kwargs):
        address = Address.objects.get(pk=kwargs.get('pk'))
        form = AddressForm(request.POST, request.FILES, instance=address)
        form.save()
        return redirect('snapdealapp:address_html')



class DeleteAddressView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Address
    template_name = 'deleteform.html'
    success_url = reverse_lazy('snapdealapp:cart')

    def has_permission(self):
        user_id = self.request.user.id
        check_user = Address.objects.get(pk=self.kwargs['pk']).user.id

        if not user_id == check_user:
            self.raise_exception = True
            success_url = reverse_lazy('snapdealapp:address_html')
            return False
        else:
            def get(self, request, *args, **kwargs):
                return self.post(request, args, kwargs)

            success_url = reverse_lazy('snapdealapp:address_html')
            return True

