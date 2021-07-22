from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Profile
from .forms import ProfileForm

from django.contrib import messages
from checkout.models import Order, OrderItem


# Create your views here.
def profile(request):
    """ 
    Display the user's profile 
    """
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please try again!')
    else:
        form = ProfileForm(instance=profile)
    orders = profile.orders.all()
    
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    orderitems = get_object_or_404(OrderItem, order=order)
    
    messages.info(request, (
        f'Your confirmation for order number # {order_number} was sent to {order.email} on {order.created_at}.'
    ))
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
        'orderitems': orderitems,
    }
    
    return render(request, template, context)