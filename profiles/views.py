from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
from checkout.models import Order, OrderItem
# import mindsdb config from settings.py
from django.conf import settings
import mindsdb_sdk
import openai
import pandas as pd
from pandas import DataFrame

# mdb_server = mindsdb_sdk.connect(settings.MINDSDB_HOST, settings.MINDSDB_EMAIL, settings.MINDSDB_PASSWORD)
# project = mdb_server.get_project('mindsdb')

# response = openai.Image.create(
#   prompt="a purple siamese cat cartoon with a yellow background",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']
# print(image_url)


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


# @login_required
# def artwork(request):
    if request.method == 'POST':
        # Retrieve the artwork description from the POST request
        artwork_description = request.POST.get('artwork_description')

        # Call your artwork generation code here
        response = openai.Image.create(
            prompt=artwork_description,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']

        # Get the user's profile
        profile = request.user.profile

        # Save the artwork and titles in the profile
        profile.artwork_description = artwork_description
        profile.artwork = image_url
        profile.titles = response['title']

        # Save the profile
        profile.save()

        # Redirect to a success page or any other desired view
        return redirect('success')

    # Render the template with the form
    return render(request, 'profiles/artwork.html')