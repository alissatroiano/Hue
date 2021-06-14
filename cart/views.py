from django.shortcuts import render, redirect, reverse, HttpResponse


# Create your views here.

def view_cart(request):
    """ A view to return the index page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ A view to add a quantity of a specific store product to the user's shopping cart """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
            cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

