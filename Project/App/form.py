from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'password1', 'password2', 'email','first_name','last_name']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderDetailsForm(ModelForm):
    class Meta:
        model = OrderDetails
        fields = '__all__'

class AddreseForm(ModelForm):
    class Meta:
        model = Addres
        fields = '__all__'