from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import AboutUs, Contact, Rule, ContactUs


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    list_display = ('address', 'email', 'phone')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Rule)
class PrivacyAdmin(TranslationAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(ContactUs)
class ContactUsAdmin(TranslationAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
# @admin.register(Terms)
# class TermsAdmin(TranslationAdmin):
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#     def has_add_permission(self, request):
#         if self.model.objects.count() >= 2:
#             return False
#         return super().has_add_permission(request)
