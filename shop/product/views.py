from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.template import loader
from product.models import Product

from resources.models import Contact


def index(request):
    products = get_list_or_404(Product)
    # print(products)
    # return HttpResponse(products)

    # slider_items = [project for project in projects if project.is_slider_item]
    template = loader.get_template('product/index.html')
    contact = Contact.objects.all()
    context = {
        'contact': contact,
        'products': products,
        # 'slider_items': slider_items,
    }
    return HttpResponse(template.render(context, request))


def men(request):
    products = Product.objects.filter(Q(type='M'))
    # print(products)
    # return HttpResponse(products)

    # slider_items = [project for project in projects if project.is_slider_item]
    template = loader.get_template('product/index.html')
    contact = Contact.objects.all()
    context = {
        'contact': contact,
        'products': products,
        # 'slider_items': slider_items,
    }
    return HttpResponse(template.render(context, request))


def women(request):
    products = Product.objects.filter(Q(type='W'))
    # print(products)
    # return HttpResponse(products)

    # slider_items = [project for project in projects if project.is_slider_item]
    template = loader.get_template('product/index.html')
    contact = Contact.objects.all()
    context = {
        'contact': contact,
        'products': products,
        # 'slider_items': slider_items,
    }
    return HttpResponse(template.render(context, request))


def child(request):
    products = Product.objects.filter(Q(type='C'))
    # print(products)
    # return HttpResponse(products)

    # slider_items = [project for project in projects if project.is_slider_item]
    template = loader.get_template('product/index.html')
    contact = Contact.objects.all()
    context = {
        'contact': contact,
        'products': products,
        # 'slider_items': slider_items,
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    template = loader.get_template('product/detail.html')
    contact = Contact.objects.all()
    return HttpResponse(template.render({'product': product, 'contact': contact}, request))
