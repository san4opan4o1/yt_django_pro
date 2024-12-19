from django.contrib import admin

# Register your models here.
from .models import Product

#trebuie sa inregistram admin
admin.site.register(Product)