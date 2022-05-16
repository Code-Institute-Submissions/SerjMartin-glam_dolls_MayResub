from django.shortcuts import render
from .models import Product
from .forms import ProductForm


def all_products(request):
    """A view to show products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def add_product(request):
    """ Add a product to the store """

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
