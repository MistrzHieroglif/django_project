from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ticket_system.models import Client

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=15)
    surname = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username','email','name','surname']



class BuyerShippingForm(UserCreationForm):
    name = forms.CharField(max_length=15)
    surname = forms.CharField(max_length=15)
    city = forms.CharField(max_length=15)
    home_number = forms.CharField(max_length=15)
    post_code = forms.CharField(max_length=15)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = Client
        fields = '__all__'

