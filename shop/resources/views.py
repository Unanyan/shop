from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def about(request):
    template = loader.get_template('resources/about.html')
    return render(request, 'resources/about.html')
