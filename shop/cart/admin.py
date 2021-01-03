from django.contrib import admin

from .models import CartItem, Cart


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'added_date')
    search_fields = ['product']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'cart_item')
    search_fields = ['user']
