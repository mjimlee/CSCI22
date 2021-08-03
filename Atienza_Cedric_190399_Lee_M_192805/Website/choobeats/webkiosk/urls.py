from django.urls import path
from . import views
from django.http import HttpResponse

app_name = 'webkiosk'
urlpatterns = [
    path('index/', views.home, name = 'home'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    #food
    path('fooditems/', views.fooditems, name='food-items'),
    path('food/add/', views.addfood, name='add-food'),
    path('food/<int:pk>/', views.fooddetails, name = 'food-details'),
    path('food/edit/<int:pk>/', views.editfood, name = 'edit-food'),
    path('food/delete/<int:pk>/', views.deletepagefood, name = 'delete-food'),
    path('food/delete/<int:pk>/confirm/', views.deletefood, name = 'delete-food-confirm'),

    #orders
    path('orders/', views.orderlist, name= 'order-list'),
    path('orders/add/', views.addorder, name= 'add-order'),
    path('orders/details/<int:pk>/', views.detailorder, name= 'detail-order'),
    path('orders/edit/<int:pk>/', views.editorder, name= 'edit-order'),
    path('orders/delete/<int:pk>/', views.deletepageorder, name = 'delete-order'),
    path('orders/delete/<int:pk>/confirm/', views.deleteorder, name = 'delete-order-confirm'),

    #customers
    path('customer/', views.customerlist, name= 'customer-list'),
    path('customer/add/', views.addcustomer, name= 'add-customer'),
    path('customer/<int:pk>/', views.customerdetails, name = 'customer-details'),
    path('customer/edit/<int:pk>/', views.editcustomer, name = 'edit-customer'),
    path('customer/delete/<int:pk>/', views.deletepagecustomer, name = 'delete-customer'),
    path('customer/delete/<int:pk>/confirm/', views.deletecustomer, name = 'delete-customer-confirm'),
]
