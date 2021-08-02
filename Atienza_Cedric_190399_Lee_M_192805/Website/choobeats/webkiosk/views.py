from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import FoodForm, OrderForm, CustomerForm, CreateUserForm, LoginForm


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

    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']

        user = authenticate(request, username=un, password=pw)

        if user is not None:
            login(request, user)
            return redirect('webkiosk:dashboard')
        else:
            message = "Your username or password is incorrect. Try again buddy!"

        # if Account.objects.filter(email=em, password=pw).exists():
        #     return render(request, 'webkiosk/dashboard.html')
        
        # else:
        #     messages.error(request, "Your username or password is incorrect. Please try again.")
        
    return render(request, 'webkiosk/login.html')

def logoutuser(request):
    logout(request)
    return redirect('webkiosk:home')

@login_required(login_url='webkiosk:login')

def dashboard(request):
    return render(request, 'webkiosk/dashboard.html')

# food functions

def fooditems(request):
    context = Food.objects.all()
    return render(request, 'webkiosk/food.html', {'fooditems':context})

# @login_required(login_url='webkiosk:login')
def addfood(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)

        name = request.POST.get('name')
        desc = request.POST.get('description')
        price = request.POST.get('price')

        if Food.objects.filter(name=name, description=desc,price=price).exists():
            messages.error(request, "You already have this exact item in your products list! Add a new one.")
        
        else:
            Food.objects.create(name=name, description=desc,price=price)
            messages.success(request, 'Successfully added.')

            return redirect('webkiosk:food-items')
    
    return render(request, 'webkiosk/addfood.html')

def fooddetails(request, pk):
    context = Food.objects.filter(pk=pk)
    return render(request, 'webkiosk/detailsfood.html', {'fooddetails':context})

def editfood(request, pk):
    context = Food.objects.filter(pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST)

        name = request.POST.get('name')
        message = request.POST.get('message')
        desc = request.POST.get('description')
        price = request.POST.get('price')

        if Food.objects.filter(name=name, description=desc, price=price).exists():
            message = "Are you sure you updated things, buddy?"
        
        else:
            Food.objects.filter(pk=pk).update(name=name, description=desc,price=price)
            messages.success(request,"Successfully edited!")
            return redirect('webkiosk:food-items')
    return render(request, 'webkiosk/editfood.html', {'editfood':context})


def deletepagefood(request,pk):
    Food.objects.filter(pk=pk)
    return render(request, 'webkiosk/deletefood.html', {'pk':pk})

def deletefood (request, pk):
    Food.objects.filter(pk=pk).delete()
    messages.error(request, 'Item successfully removed.')
    return redirect('webkiosk:food-items')

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
            messages.success(request, 'Got the edit/s boss!')
    context = {'form': form}
    return render(request, 'webkiosk/food.html', context)

# order functions
def orderlist(request):
    context = {'orders': Order.objects.all()}
    return render(request, 'webkiosk/orders.html', context)

# @login_required(login_url='webkiosk:login') WORK ON THIS
def addorder(request):
    # message = ""
    # if request.method == 'POST':
    #     form = FoodForm(request.POST)

    #     cust = request.POST.get('customer')
    #     food = request.POST.get('food')
    #     quant = request.POST.get('quantity')
    #     pm = request.POST.get('paymode')

    #     if Customer.objects.filter(paymentmode=pm, customer=cust,food=food, quantity = quant).exists():
    #         message = "You already have this exact item in your products list! Add a new one."
        
    #     else:
    #         Food.objects.create(name=name, description=desc,price=price)
    #         return redirect('webkiosk:food-items')
    return render(request, 'webkiosk/addfood.html')

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
# customers
        # fields = ['firstname', 'lastname', email 'address', 'city'] province

def customerlist(request):
    context = Customer.objects.all()
    return render(request, 'webkiosk/customers.html', {'customerlist':context})

# @login_required(login_url='webkiosk:login')
def addcustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        num = request.POST.get('num')
        ad = request.POST.get('ad')
        city = request.POST.get('city')
        prov = request.POST.get('prov')

        if Customer.objects.filter(firstname=fname, lastname=lname,email=email, number=num, address=ad, city=city, province=prov).exists():
            messages.error(request,"You already have this exact customer in your customer list! Add a new one.")
        
        else:
            Customer.objects.create(firstname=fname, lastname=lname,email=email, number=num, address=ad, city=city, province=prov)
            messages.success(request,"Successfully added!")

            return redirect('webkiosk:customer-list')
    
    return render(request, 'webkiosk/addcustomer.html')

def customerdetails(request, pk):
    context = Customer.objects.filter(pk=pk)
    return render(request, 'webkiosk/detailscustomer.html', {'customerdetails':context})

def editcustomer(request, pk):
    context = Customer.objects.filter(pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        num = request.POST.get('num')
        ad = request.POST.get('ad')
        city = request.POST.get('city')
        prov = request.POST.get('prov')

        if Customer.objects.filter(firstname=fname, lastname=lname,email=email, number=num, address=ad, city=city, province=prov).exists():
            messages.error(request,"You didn't make any changes!")

        
        else:
            Customer.objects.filter(pk=pk).update(firstname=fname, lastname=lname,email=email, number=num, address=ad, city=city, province=prov)
            messages.success(request,"Successfully updated!")

            return redirect('webkiosk:customer-list')
    return render(request, 'webkiosk/editcustomer.html', {'editcustomer':context})

def deletepagecustomer(request,pk):
    Customer.objects.filter(pk=pk)
    return render(request, 'webkiosk/deletecustomer.html', {'pk':pk})

def deletecustomer (request, pk):
    Customer.objects.filter(pk=pk).delete()
    messages.error(request, 'Customer successfully removed.')

    return redirect('webkiosk:customer-list')
