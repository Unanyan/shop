from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import loader

from product.models import Product

from users.models import Customer


class CartItem(models.Model):
    product = models.ForeignKey(
        Product, related_name='product', on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.__str__() + ': ' + self.quantity.__str__()


# @receiver(post_save, sender=CartItem)
# def update_model(sender, instance, **kwargs):
#     if kwargs['created']:
#         quantity = instance.quantity
#         instance.product.count -= quantity
#         instance.product.save()
#         print('productCount: ', instance.product.count)


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


@receiver(post_save, sender=Cart)
def update_model(sender, instance, **kwargs):
    if kwargs['created']:
        user = instance.user
        cart_item = instance.cart_item
        quantity = cart_item.quantity
        product = cart_item.product
        product_link = 'http://127.0.0.1:8000/en/' + str(product.id)
        message = (user.name + '\n' + user.address + '\n' + user.phone + '\n\n' +
                   product.name + ': ' + str(quantity) + '\n' +
                   product_link)
        subject, from_email = 'New order', 'presents.shop.vanadzor@gmail.com'
        #
        # print("Sending notification to admin")
        #
        # send_mail(subject, message, from_email, ['unanyanmeruzan@gmail.com'])

        html_message = loader.render_to_string(
            'mailing/admin.html',
            {
                'product_link': product_link,
                'product': product,
                'user': user,
                'quantity': quantity,
            }
        )
        send_mail(subject, message, from_email, ['unanyanmeruzan@gmail.com'], fail_silently=True, html_message=html_message)

        product.count -= quantity
        product.save()
        print('productCount: ', product.count)
