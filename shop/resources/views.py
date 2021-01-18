from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Contact, Rule, AboutUs, ContactUs


def about(request):
    about_us = AboutUs.objects.all()
    contact = Contact.objects.all()
    template = loader.get_template('resources/about.html')

    return HttpResponse(template.render({'about_us': about_us, 'contact': contact}, request))


def how_to_order(request):
    contact = Contact.objects.all()
    rule = Rule.objects.all()

    return render(request, 'resources/rules.html', {'contact': contact, 'rule': rule})


def contact_us(request):
    contact = Contact.objects.all()
    contact_uss = ContactUs.objects.all()

    return render(request, 'resources/contact_us.html', {'contact': contact, 'contact_us': contact_uss})
#
#
# def terms_and_conditions(request):
#     contact = Contact.objects.all()
#     terms = Terms.objects.all()
#
#     return render(request, 'resources/terms.html', {'contact': contact, 'terms': terms})
