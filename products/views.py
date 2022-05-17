from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


def all_products(request):
    """A view to show products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


@login_required
def add_product(request):
    """ Add a voucher to the store only by authorized person"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products'))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, item_id):
    """ Edit product on admin page only by authorized person"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=item_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('products'))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:

        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, item_id):
    """ Edit product on admin page only by authorized person"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only owners can do that.')
        return redirect(reverse('home'))

    product = Product.objects.get(pk=item_id)
    product.delete()
    messages.success(request, 'Product deleted!')

    return redirect(reverse('products'))
