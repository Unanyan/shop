from ckeditor.fields import RichTextField
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from users.models import Subscriber


class Category(models.Model):
    MEN = 'M'
    WOMEN = 'W'
    CHILD = 'C'
    TYPE_CHOICES = [
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (CHILD, 'Child'),
    ]

    title = models.CharField(max_length=25, default='mix')

    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=CHILD,
    )

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title + self.type


class Product(models.Model):
    MEN = 'M'
    WOMEN = 'W'
    CHILD = 'C'
    TYPE_CHOICES = [
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (CHILD, 'Child'),
    ]

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='')
    content = RichTextField(blank=True) #null=False, default='')
    is_slider_item = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=CHILD,
    )

    def __str__(self):
        return self.name

    def get_default_image(self):
        images_list = self.images.filter(default=True)

        if len(images_list):
            return images_list[0].image.url

    def get_images(self):
        images_list = self.images.filter()#default=False)
        return images_list.all()

    def get_images_count(self):
        return self.get_images().count()

    def get_absolute_url(self):
        return reverse('product:detail', args=[str(self.id)])


class Gallery(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.product.name


@receiver(post_save, sender=Product)
def send_email(sender, instance, **kwargs):
    if kwargs['created']:
        message = ('We are created new product!\n\n  The new product name is: ' +
                   instance.name + ',\n  Description is: ' + instance.description + '.')
        subject, from_email = 'New Post', 'presents.shop.vanadzor@gmail.com'

        print("Sending notifications this emails from subscribers: ")

        for subscriber in Subscriber.objects.all():
            print(subscriber.mail)
            send_mail(subject, message, from_email, [subscriber.mail])
