from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
    context = Order.objects.all()[:3]
    return render(request, 'webkiosk/dashboard.html', {'orderlist':context})

# food functions

def fooditems(request):
    context = Food.objects.all()
    return render(request, 'webkiosk/food.html', {'fooditems':context})

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

# def editfood(request, pk):
#     context = Food.objects.filter(pk=pk)
#     if request.method == 'POST':
#         form = FoodForm(request.POST)

#         name = request.POST.get('name')
#         desc = request.POST.get('description')
#         price = request.POST.get('price')

#         if Food.objects.filter(name=name, description=desc, price=price).exists():
#             messages.error(request, "Are you sure you updated things, buddy?")
        
#         else:
#             Food.objects.filter(pk=pk).update(name=name, description=desc,price=price)
#             messages.success(request,"Successfully edited!")
#             return redirect('webkiosk:food-items')

#     return render(request, 'webkiosk/editfood.html', {'editfood':context})

def editfood(request, pk):
    context = Food.objects.filter(pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST)

        name = request.POST.get('name')
        desc = request.POST.get('description')
        price = request.POST.get('price')

        if Food.objects.filter(name=name, description=desc,price=price).exists():
            messages.error(request, "You did not make any changes ngek")
        
        else:
            Food.objects.filter(pk=pk).update(name=name, description=desc,price=price)
            messages.success(request, 'Successfully updated.')

            return redirect('webkiosk:food-items')
    
    return render(request, 'webkiosk/editfood.html', {'editfood':context})


def deletepagefood(request,pk):
    Food.objects.filter(pk=pk)
    return render(request, 'webkiosk/deletefood.html', {'pk':pk})

def deletefood (request, pk):
    Food.objects.filter(pk=pk).delete()
    messages.error(request, 'Item successfully removed.')
    return redirect('webkiosk:food-items')

def detailfood(request, pk):
    food = Food.objects.get(id=pk)
    context = {'food': food}
    return render(request, 'webkiosk/food.html', context)
    
# order functions

def orderlist(request):
    context = Order.objects.all()
    return render(request, 'webkiosk/orders.html', {'orderlist':context})

def addorder(request):
    allfood = Food.objects.all()
    allcustomer = Customer.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)

        cust = get_object_or_404(Customer, pk=request.POST.get('customer'))
        food = get_object_or_404(Food, pk=request.POST.get('food'))
        quant = request.POST.get('quantity')
        pm = request.POST.get('paymentmode')

        if Order.objects.filter(customer=cust, food=food, quantity=quant, paymentmode=pm).exists():
            messages.error(request,"You already have this exact order.")
        
        else:
            Order.objects.create(customer=cust, food=food, quantity=quant, paymentmode=pm)
            messages.success(request,"Successfully added!")

            return redirect('webkiosk:order-list')
    
    return render(request, 'webkiosk/addorders.html', {'foods':allfood, 'customers':allcustomer})

def detailorder(request, pk):
    order = Order.objects.get(id=pk)
    context ={'order': order}
    return render(request, 'webkiosk/detailsorder.html', context)

def editorder(request, pk):
    allfood = Food.objects.all()
    allcustomer = Customer.objects.all()
    context = Order.objects.filter(pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)

        cust = get_object_or_404(Customer, pk=request.POST.get('customer'))
        food = get_object_or_404(Food, pk=request.POST.get('food'))
        quant = request.POST.get('quantity')
        pm = request.POST.get('paymentmode')

        if Order.objects.filter(customer=cust, food=food, quantity=quant, paymentmode=pm).exists():
            messages.error(request,"You did not make any changes.")
        
        else:
            Order.objects.filter(pk=pk).update(customer=cust, food=food, quantity=quant, paymentmode=pm)
            messages.success(request,"Successfully updated!")

            return redirect('webkiosk:order-list')
    
    return render(request, 'webkiosk/editorder.html', {'foods':allfood, 'customers':allcustomer, 'editorder':context})

def deletepageorder(request,pk):
    Order.objects.filter(pk=pk)
    return render(request, 'webkiosk/deleteorder.html', {'pk':pk})

def deleteorder (request, pk):
    Order.objects.filter(pk=pk).delete()
    messages.error(request, 'Item successfully removed.')
    return redirect('webkiosk:order-list')

# customer functions
# customers
        # fields = ['firstname', 'lastname', email 'address', 'city'] province

def customerlist(request):
    context = Customer.objects.all()
    return render(request, 'webkiosk/customers.html', {'customerlist':context})

def addcustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        ad = request.POST.get('ad')
        city = request.POST.get('city')
        prov = request.POST.get('prov')

        if Customer.objects.filter(firstname=fname, lastname=lname,email=email, address=ad, city=city, province=prov).exists():
            messages.error(request,"You already have this exact customer in your customer list! Add a new one.")
        
        else:
            Customer.objects.create(firstname=fname, lastname=lname,email=email, address=ad, city=city, province=prov)
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

        if Customer.objects.filter(firstname=fname, lastname=lname,email=email, address=ad, city=city, province=prov).exists():
            messages.error(request,"You didn't make any changes!")

        else:
            Customer.objects.filter(pk=pk).update(firstname=fname, lastname=lname,email=email, address=ad, city=city, province=prov)
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