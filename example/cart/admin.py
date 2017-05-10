from django.contrib import admin
from .models import Customer, Cart_Item

# Register your models here.
admin.site.register(Customer)
admin.site.register(Cart_Item)