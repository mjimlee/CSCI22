"""choobeats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.http import HttpResponse

app_name = 'webkiosk'
urlpatterns = [

    path('index/', views.home, name = 'home'),

    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    #log in page missing
    path('logout/', views.logoutuser, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    #food
    path('fooditems/', views.fooditems, name='food-items'),
    path('food/add/', views.addfood, name='add-food'),

    #orders
    path('orders/', views.orderlist, name= 'order-list'),
    path('orders/add/', views.addorder, name= 'add-order'),

    #customers
    path('customer/', views.customerlist, name= 'customer-list'),
    path('customer/add/', views.addcustomer, name= 'add-customer'),

    path('delete/', views.delete, name = 'delete')


]
