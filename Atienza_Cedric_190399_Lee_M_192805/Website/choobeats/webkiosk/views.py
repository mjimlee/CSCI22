from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Food, Customer, Order
from .forms import FoodForm, OrderForm, CustomerForm, CreateUserForm

def home(request):
    return render(request, 'webkiosk/index.html')

def registerpage(request):
    if request.method == 'GET':
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'webkiosk/register.html', context)
    elif request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webkiosk/dashboard.html')

def loginpage(request):
    if request.method == 'GET':
        form = FoodForm()
        context = {'form': form}
        return render(request, 'webkiosk/signin.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('webkiosk:dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('webkiosk:index')
            else:
                messages.info(request, 'Type your username and password again. You can do it buddy! ')

        context = {}
        return render(request, 'webkiosk/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('webkiosk:login')

# @login_required(login_url='webkiosk:login')
def dashboard(request):
    return render(request, 'webkiosk/dashboard.html')

# food functions
# @login_required(login_url='webkiosk:login')
def fooditems(request):
    context = {'fooditems': Food.objects.all()}
    return render(request, 'webkiosk/food.html', context)

# @login_required(login_url='webkiosk:login')
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

# @login_required(login_url='webkiosk:login')
def detailfood(request, pk):
    food = Food.objects.get(id=pk)
    context = {'food': food}
    return render(request, 'webkiosk/food.html', context)

# @login_required(login_url='webkiosk:login')
def editfood(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        form = FoodForm(instance=food)
    elif request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Got the edits boss!')
    context = {'form': form}
    return render(request, 'webkiosk/food.html', context)


# order functions
def orderlist(request):
    context = {'orders': Order.objects.all()}
    return render(request, 'webkiosk/orders.html', context)

# @login_required(login_url='webkiosk:login')
def addorder(request):
    if request.method == 'GET':
        form = OrderForm()
        context = {'form': form}
        return render(request, 'webkiosk/addorders.html', context)

# @login_required(login_url='webkiosk:login')
def detailorder(request, pk):
    order = Order.objects.get(id=pk)
    context ={'order': order}
    return render(request, 'webkiosk/order.html', context)

# @login_required(login_url='webkiosk:login')
def editorder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'GET':
       form = OrderForm(instance=order)
    elif request.method == 'POST':
         form = OrderForm(request.POST, instance=order)
         if form.is_valid():
             form.save()
             messages.success(request, 'I got the order, boss!')
    context = {'form':form}
    return render(request, 'webkiosk/order.html', context)

# customer functions
def customerlist(request):
    context = {'customerlist': Customer.objects.all()}
    return render(request, 'webkiosk/customers.html', context)

# @login_required(login_url='webkiosk:login')
def addcustomer(request):
    if request.method == 'GET':
        form = CustomerForm()
        context = {'form': form}
        return render(request, 'webkiosk/addcustomer.html', context)

# @login_required(login_url='webkiosk:login')
def detailcustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    context ={'customer': customer}
    return render(request, 'webkiosk/customers.html', context)

# @login_required(login_url='webkiosk:login')
def updatecustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
       form = CustomerForm(instance=customer)
    elif request.method == 'POST':
         form = CustomerForm(request.POST, instance=customer)
         if form.is_valid():
             form.save()
             messages.success(request, 'New Customer in our family!')
    context = {'form':form}
    return render(request, 'webkiosk/customers.html', context)

# @login_required(login_url='webkiosk:login')
def deletecustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
        context = {'customer':customer}
        return render(request, 'webkiosk/customers.html', context)
    elif request.method == 'POST':
        customer.delete()
        return redirect('webkiosk:customers')
