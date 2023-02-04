from django.contrib import admin
from .models import Category,Brand, Firm,Product,Purchases,Sales

# Register your models here.

admin.site.register((Category,Brand, Firm,Product,Purchases,Sales))
