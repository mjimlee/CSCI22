from django.contrib import admin
from .models import Customer, Food, Order, Account

admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(Account)