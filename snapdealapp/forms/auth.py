from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    mobileno = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                help_text = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))


    class Meta:
        model = User
        fields = ('username', 'mobileno','email', 'password1', 'password2', )


class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name'})
    )
    password = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
