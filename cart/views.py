from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from shop.models import Product

# Create your views here.

def view_cart(request):
    """ A view to return the index page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ A view to add a quantity of a specific store product to the user's shopping cart """
    
    product = get_object_or_404(Product, pk=item_id)
   
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    dimension = None
    if 'product_dimension' in request.POST:
         dimension = request.POST['product_dimension']
    cart = request.session.get('cart', {})

    if dimension:
        if item_id in list(cart.keys()):
            if dimension in cart[item_id]['items_by_dimension'].keys():
                cart[item_id]['items_by_dimension'][dimension] += quantity
                messages.success(request,
                                 (f'Updated dimension {dimension.upper()} '
                                  f'{product.title} quantity to '
                                  f'{cart[item_id]["items_by_dimension"][dimension]}'))
            else:
                 cart[item_id]['items_by_dimension'][dimension] = quantity
                 messages.success(request,
                                 (f'Added dimension {dimension.upper()} '
                                  f'{product.title} to your cart'))
        else:
            cart[item_id] = {'items_by_dimension': {dimension: quantity}}
            messages.success(request,
                             (f'Added dimension {dimension.upper()} '
                              f'{product.title} to your cart'))

    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.title} '
                              f'quantity to {cart[item_id]}'))
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.title} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    dimension = None

    if 'product_dimension' in request.POST:
        dimension = request.POST['product_dimension']
    cart = request.session.get('cart', {})

    if dimension:
        if item_id in list(cart.keys()):
            if dimension in cart[item_id]['items_by_dimension'].keys():
                cart[item_id]['items_by_dimension'][dimension] += quantity
                messages.success(request,
                                 (f'Updated dimension {dimension.upper()} '
                                  f'{product.title} quantity to '
                                  f'{cart[item_id]["items_by_dimension"][dimension]}'))

        if quantity > 0:
            cart[item_id]['items_by_dimension'][dimension] = quantity
        else:
            del cart[item_id]['items_by_dimension'][dimension]
            if not cart[item_id]['items_by_dimension']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        dimension = None
        if 'product_dimension' in request.POST:
            dimension = request.POST['product_dimension']
        cart = request.session.get('cart', {})

        if dimension:
            del cart[item_id]['items_by_dimension'][dimension]
            if not cart[item_id]['items_by_dimension']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


