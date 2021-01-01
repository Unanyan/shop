from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Contact, Rule, AboutUs


def about(request):
    about_us = AboutUs.objects.all()
    contact = Contact.objects.all()
    template = loader.get_template('resources/about.html')

    return HttpResponse(template.render({'about_us': about_us, 'contact': contact}, request))


def privacy_and_policy(request):
    contact = Contact.objects.all()
    rule = get_object_or_404(Rule, title_en__icontains='privacy')

    return render(request, 'resources/rules.html', {'contact': contact, 'rule': rule})


def terms_and_conditions(request):
    contact = Contact.objects.all()
    rule = get_object_or_404(Rule, title_en__icontains='term')
