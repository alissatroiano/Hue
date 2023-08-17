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
from hugo.models import Artwork
from hugo.forms import ArtworkForm


def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    artworks = Artwork.objects.filter(user=request.user).order_by('-created_at')

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
        'on_profile_page': True,
        'artworks': artworks,
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
        'default_town_or_city': profile.default_town_or_city,
        'default_country': profile.default_country or 'United States',
    }

    return render(request, template, context)


def edit_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id, user=request.user)

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page or any other desired page
    else:
        form = ArtworkForm(instance=artwork)

    template = 'profiles/edit_artwork.html'
    context = {
        'form': form,
        'artwork': artwork,
    }

    return render(request, template, context)


def delete_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id, user=request.user)
    
    if request.method == 'POST':
        artwork.delete()
        # Redirect to the user's profile page
        return redirect('profile')

    template = 'profiles/delete_artwork.html'
    context = {
        'artwork': artwork,
    }
    return render(request, template, context)