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
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
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
        images_list = self.images.filter(default=False)
        return images_list.all()

    def get_images_count(self):
        return self.get_images().count()


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
