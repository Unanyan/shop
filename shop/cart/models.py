from django.db import models

from product.models import Product

from users.models import Customer


class CartItem(models.Model):
    product = models.ForeignKey(
        Product, related_name='product', on_delete=models.CASCADE
    )
    quantity= models.IntegerField()
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.__str__() + ': ' + self.quantity.__str__()


class Cart(models.Model):
    user = models.ForeignKey(
        Customer, related_name='customer', on_delete=models.CASCADE
    )
    cart_item = models.ForeignKey(
        CartItem, related_name='cart_item', on_delete=models.CASCADE
    )
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return self.user.__str__() + self.cart_item.__str__()
