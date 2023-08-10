from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm, AvatarForm
from django.contrib import messages
from checkout.models import Order, OrderItem
# import mindsdb config from settings.py
from django.conf import settings
import mindsdb_sdk
import openai
import pandas as pd
from pandas import DataFrame


# Create your views here.

def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    avatar_form = AvatarForm(request.POST or None, request.FILES or None, instance=profile)
    form = ProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        if avatar_form.is_valid():
            avatar_form.save()
            messages.success(request, 'Avatar updated successfully')
        elif form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please try again!')

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'avatar_form': avatar_form,
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
         'default_town_or_city': profile.default_town_or_city,  # Add this line
        'default_country': profile.default_country  # Add this line
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