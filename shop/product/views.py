from django.http import HttpResponse
from django.shortcuts import get_list_or_404

from product.models import Product


def index(request):
    products = get_list_or_404(Product)
    print(products)
    return HttpResponse(products)
