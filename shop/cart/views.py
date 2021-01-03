from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views.decorators.http import require_POST
from product.models import Product
from .cart import Cart as CartSession
from .forms import CartAddProductForm
from resources.models import Contact

from users.models import Customer

from .models import CartItem, Cart


@require_POST
def cart_add(request, product_id):
    cart = CartSession(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        # print(cd['quantity'])
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
    print(request.session['cart'])
    return HttpResponse(template.render({'cart': cart, 'contact': contact}, request))
    # return render(request, 'cart/detail.html', {'cart': cart})


def checkout(request):
    # email = request.POST['email']
    # try:
    #     if request.method == 'POST':
            # if exist try exception
    #         Subscriber.objects.get(mail=email)
    #         print("Subscriber with this email exist: ", email)
    #     messages.success(request, 'Thank you, you are already subscribed!')
    #     return HttpResponseRedirect('/', {'email': email.__str__()})
    # except Subscriber.DoesNotExist as i:
    #     try:
    #         validate_email(email)
    #         sub = Subscriber()
    #         sub.mail = email
    #         sub.save()
    #         print("Created subscriber with this email: ", email, i)
    #         messages.success(request, 'Thank you, you are successfully subscribed!')
    #         return HttpResponseRedirect('/')
    #     except ValidationError as e:
    #         print("bad email, details: ", e)
    #         messages.success(request, 'Please input correct email!')
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        customer = Customer()
        customer.mail = email
        customer.name = name
        customer.address = address
        customer.phone = phone
        customer.save()

        cart_session = CartSession(request)


        from django.forms.models import model_to_dict

        # data = self.get_queryset()

        for item in cart_session:
            cart_item = CartItem()
            print('item', item)
            # item['product'] = model_to_dict(item['product'])
            # cart_item.product = get_object_or_404(Product, id=item['product']['id'])
            cart_item.product = item['product']
            cart_item.quantity = item['quantity']
            cart_item.save()
            cart = Cart()
            cart.user = customer
            cart.cart_item = cart_item
            cart.save()
        return HttpResponseRedirect('/')
    else:
        contact = Contact.objects.all()
        return render(request, 'cart/checkout.html', {'contact': contact,})
