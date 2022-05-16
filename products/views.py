from django.shortcuts import render, redirect, reverse
from django.contrib import messages
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
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products'))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, item_id):
    """ Edit product on admin page """
    product = Product.objects.get(pk=item_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('products'))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')
    else:

        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
