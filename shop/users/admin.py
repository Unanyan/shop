from django.contrib import admin

from .models import Subscriber, Customer


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('mail', 'added_date')
    search_fields = ['mail']


@admin.register(Customer)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'address')
    search_fields = ['mail']
