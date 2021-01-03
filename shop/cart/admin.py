from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CartItem, Cart


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'added_date')
    search_fields = ['product']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'cart_item', 'cart_item_image_show', 'is_shipped')
    search_fields = ['user']

    def cart_item_image_show(self, obj):
        cart_item = obj.cart_item
        if cart_item:
            def_image = cart_item.product.images.filter(default=True)
            return mark_safe("<img src='{}' width='60' />".format(def_image[0].image.url))
        return "None"
