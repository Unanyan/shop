from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.template import loader
from product.models import Product

from resources.models import Contact

from cart.forms import CartAddProductForm

from .models import Category


def index(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category_id', None)
    if category_id:
        products = Product.objects.filter(Q(category_id=category_id)).filter(Q(count__gt=0))
    else:
        products = Product.objects.filter(Q(is_slider_item=True)).filter(Q(count__gt=0))[:30]
        # products = get_list_or_404(Product)
    # print(products)
    # return HttpResponse(products)

    # slider_items = [project for project in projects if project.is_slider_item]
    template = loader.get_template('product/index.html')
    contact = Contact.objects.all()
    context = {
        'from_index': True,
        'contact': contact,
        'products': products,
        'categories': categories,
        # 'slider_items': slider_items,
    }
    if request.is_ajax():
        products_section = loader.render_to_string('product/products.html',
                                                   {'products': products},
                                                   request=request)
        return JsonResponse({'products': products_section})

    return HttpResponse(template.render(context, request))


def men(request):
    categories = Category.objects.filter(Q(type='M'))
    category_id = request.GET.get('category_id', None)
    if category_id:
        products = Product.objects.filter(Q(category_id=category_id)).filter(Q(count__gt=0))
    else:
        products = Product.objects.filter(Q(type='M')).filter(Q(count__gt=0))
    # print(products)
    # return HttpResponse(products)

    # slider_items = [project for project in projects if project.is_slider_item]
    template = loader.get_template('product/index.html')
    contact = Contact.objects.all()
    context = {
        'contact': contact,
        'products': products,
        'categories': categories,
        # 'slider_items': slider_items,
    }

    if request.is_ajax():
        products_section = loader.render_to_string('product/index.html',
                                                   {'products': products},
                                                   request=request)
        return JsonResponse({'products': products_section})

    return HttpResponse(template.render(context, request))


def women(request):
    categories = Category.objects.filter(Q(type='W'))
    category_id = request.GET.get('category_id', None)
    if category_id:
        products = Product.objects.filter(Q(category_id=category_id)).filter(Q(count__gt=0))
    else:
        products = Product.objects.filter(Q(type='W')).filter(Q(count__gt=0))
    # print(products)
    # return HttpResponse(products)

    # slider_items = [project for project in projects if project.is_slider_item]
    template = loader.get_template('product/index.html')
    contact = Contact.objects.all()
    context = {
        'contact': contact,
        'products': products,
        'categories': categories,
        # 'slider_items': slider_items,
    }

    if request.is_ajax():
        products_section = loader.render_to_string('product/index.html',
                                                   {'products': products},
                                                   request=request)
        return JsonResponse({'products': products_section})

    return HttpResponse(template.render(context, request))


def child(request):
    categories = Category.objects.filter(Q(type='C'))
    category_id = request.GET.get('category_id', None)
    if category_id:
        products = Product.objects.filter(Q(category_id=category_id)).filter(Q(count__gt=0))
    else:
        products = Product.objects.filter(Q(type='C')).filter(Q(count__gt=0))
    # print(products)
    # return HttpResponse(products)

    # slider_items = [project for project in projects if project.is_slider_item]
    template = loader.get_template('product/index.html')
    contact = Contact.objects.all()
    context = {
        'categories': categories,
        'contact': contact,
        'products': products,
        # 'slider_items': slider_items,
    }

    if request.is_ajax():
        products_section = loader.render_to_string('product/index.html',
                                                   {'products': products},
                                                   request=request)
        return JsonResponse({'products': products_section})

    return HttpResponse(template.render(context, request))


def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    template = loader.get_template('product/detail.html')
    contact = Contact.objects.all()
    cart_product_form = CartAddProductForm()
    return HttpResponse(template.render({'product': product, 'contact': contact, 'cart_product_form': cart_product_form}, request))
