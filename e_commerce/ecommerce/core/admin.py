from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Customer,Product,Order,OrderItem,ShippingAddress)
class admin_class(admin.ModelAdmin):
    pass