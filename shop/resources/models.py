from ckeditor.fields import RichTextField
from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class AboutUs(models.Model):
    title = models.CharField(default='About us', max_length=155)
    what_we_do = RichTextField(null=False)
    our_team = RichTextField(null=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Rule(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField(null=False)

    def __str__(self):
        return self.title


class Terms(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField(null=False)

    def __str__(self):
        return self.title
