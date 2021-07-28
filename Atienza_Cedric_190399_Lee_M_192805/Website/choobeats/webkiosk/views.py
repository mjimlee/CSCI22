from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Food, Customer, Order
from .forms import FoodForm, OrderForm, CustomerForm, CreateUserForm

def registernewuser(request):
    if request.user.is_authenticated:
        return redirect('webkiosk:index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('webkiosk:login')
        context = {'form':form}
        return render(request, 'webkiosk/register.html', context)

# add log in page

def logoutuser(request):
    logout(request)
    return redirect('webkiosk:index')

# add log in restrictions
def dashboard(request):
    return render(request, 'webkiosk/dashboard.html')

# add log in restrictions
def fooditems(request):
    context = {'fooditems': Food.objects.all()}
    return render(request, 'webkiosk/food.html', context)

# add log in restrictions
def addfood(request):
    if request.method == 'GET':
        form = FoodForm()
        context = {'form': form}
        return render(request, 'webkiosk/addfood.html', context)
    elif request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:fooditems')

