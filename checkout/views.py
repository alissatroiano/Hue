from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderItem

from shop.models import Product
from cart.contexts import cart_components

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'user_full_name': request.POST['user_full_name'],
            'street_address': request.POST['street_address'],
            'city': request.POST['city'],
            'state': request.POST['state'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'zip_code': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            }


    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('shop'))
    current_cart = cart_components(request)
    total = current_cart['grand_total']
    # stripe
    stripe_total = round(total * 100)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
)
    print(intent)

    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
    'order_form': order_form,
    'stripe_public_key': 'pk_test_51J5BfyJuLUUDUAz9Rkhvu4bi7GFnV0T1E3ueMvoUlFvU6OCJOCWhYG3LFRmeTvTFyUvb0CyF6W8uALTdnuYhUSJD00AL9gibGI',
    'client_secret': 'test client secret',
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)