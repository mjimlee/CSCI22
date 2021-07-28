from django.contrib import admin
from .models import Customer, Food, Order

admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(Order)