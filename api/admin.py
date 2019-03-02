from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    pass

