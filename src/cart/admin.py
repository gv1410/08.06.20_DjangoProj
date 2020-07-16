from django.contrib import admin
from .models import Cart, BookInCart

# Register your models here.

admin.site.register(Cart)
admin.site.register(BookInCart)
