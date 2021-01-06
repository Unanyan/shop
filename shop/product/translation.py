from modeltranslation.translator import register, TranslationOptions

from .models import Product, Category


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    required_languages = ('en', 'hy')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('en', 'hy')
