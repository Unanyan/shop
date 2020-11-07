from ckeditor.fields import RichTextField
from django.db import models


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
    image = models.ImageField(upload_to="images/")
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=CHILD,
    )

    def __str__(self):
        return self.name
