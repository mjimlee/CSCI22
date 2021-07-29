from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Customer, Food, Order

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'address', 'city']
        
class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'food', 'quantity','paymentmode']
