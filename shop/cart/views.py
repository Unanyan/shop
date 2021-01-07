from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views.decorators.http import require_POST
from product.models import Product
from .cart import Cart as CartSession
from .forms import CartAddProductForm
from resources.models import Contact

from django.contrib import messages

from users.models import Customer

from .models import CartItem, Cart
from django.utils.translation import ugettext as _


@require_POST
def cart_add(request, product_id):
    cart = CartSession(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print('cd: ', cd['quantity'])
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = CartSession(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = CartSession(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    template = loader.get_template('cart/detail.html')
    contact = Contact.objects.all()
    print('cart: ', request.session['cart'])
    return HttpResponse(template.render({'cart': cart, 'contact': contact}, request))
    # return render(request, 'cart/detail.html', {'cart': cart})


def checkout(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        customer = Customer()
        customer.name = name
        customer.address = address
        customer.phone = phone
        customer.save()

        cart_session = CartSession(request)

        for item in cart_session:
            cart_item = CartItem()
            print('item', item)

            from django.forms.models import model_to_dict

            item['product'] = model_to_dict(item['product'])
            cart_item.product = get_object_or_404(Product, id=item['product']['id'])

            print(',,,', item['quantity'], item['product']['count'])
            print('request', request.__str__())
            cart_item.quantity = item['quantity']
            cart_item.save()
            if item['quantity'] > item['product']['count']:
                # messages.success(request, 'Quantity greater than we have!')
                return HttpResponseRedirect('/')
            cart = Cart()
            cart.user = customer
            cart.cart_item = cart_item
            cart.save()
        messages.success(request, _('Your order has been successfully accepted!'))
        return HttpResponseRedirect('/')
    else:
        messages.success(request, _('Please fill in all the fields!'))
        contact = Contact.objects.all()
        return render(request, 'cart/checkout.html', {'contact': contact,})
