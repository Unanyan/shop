from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.contrib import admin
from .models import Product, Gallery


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 0


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = (
        'name', 'image_show', 'description', 'content', 'price', 'count', 'is_slider_item', 'type'
    )
    list_filter = ('name', 'price', 'count', 'type')
    search_fields = ['name',]
    inlines = [GalleryInline,]

    def image_show(self, obj):
        def_image = obj.images.filter(default=True)
        if def_image:
            return mark_safe("<img src='{}' width='60' />".format(def_image[0].image.url))
        return "None"

    image_show.__name__ = "default_image"

