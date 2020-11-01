from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to see all products """

    products = Product.object.all()

    context = {
        'products': products
    }
