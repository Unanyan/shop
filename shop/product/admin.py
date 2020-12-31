from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.contrib import admin
from .models import Product, Gallery


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 0


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = (
        'name', 'description', 'content', 'price', 'count', 'is_slider_item', 'type'
    )
    list_filter = ('name', 'price', 'count', 'type')
    search_fields = ['name',]
    inlines = [GalleryInline,]

