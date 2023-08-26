import os
import re
from django.core import files
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .forms import ArtworkForm
from .models import Artwork, Style
from django.conf import settings
from django.contrib import messages
import mindsdb_sdk
from django.core.files.temp import NamedTemporaryFile
import requests
import openai
import pandas as pd
from pandas import DataFrame
import random
import string
import time
email = os.environ["MINDSDB_EMAIL"]
password = os.environ["MINDSDB_PASSWORD"]

from cart.views import add_to_cart

def hugo(request):
    artworks = Artwork.objects.all()
    styles = None

    # sort artwork by style if the user has selected that style
    if request.GET:
        style_param = request.GET['style']
        if style_param == 'photography':
            photography_artworks = artworks.filter(style__name='photography')
            context = {
                'artworks': photography_artworks,
                'current_styles': 'photography',  # Set this to 'photography' for highlighting in the template
            }
            return render(request, 'photography.html', context)
        else:
            artworks = artworks.exclude(style__name='photography')
            styles = Style.objects.filter(name__in=styles)
    # display artwork from newest to oldest whe visiting the page
    artworks = artworks.order_by('-created_at')
    context = {
        'artworks': artworks,
        'current_styles': styles,
        # 'sort_dir': sort_dir,
    }

    return render(request, 'hugo.html', context)


def photo_art(request):
    artworks = Artwork.objects.all()
    styles = None

    artworks = artworks.order_by('-created_at')
    context = {
        'artworks': artworks,
        'current_styles': styles,
        # 'sort_dir': sort_dir,
    }

    return render(request, 'hugo.html', context)


def artwork_detail(request, artwork_id):
    """ A view to render a page for individual artwork and artwork details """
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artwork_detail.html', context)

@login_required
def add_hugo(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.user = request.user
            artwork.save()
            
            style = artwork.style  # Get the selected style from the artwork object
            text = artwork.artwork_description
            
            mdb_server = mindsdb_sdk.connect('https://cloud.mindsdb.com', settings.MINDSDB_EMAIL, settings.MINDSDB_PASSWORD)
            project = mdb_server.get_project('open_ai')
            
            if style.name == 'pop-art':
                query = project.query(f'SELECT * FROM open_ai.retro WHERE text="{text}";')
            elif style.name == 'digital-art':
                query = project.query(f'SELECT * FROM open_ai.digital_only WHERE text="{text}";')
            elif style.name == 'fine-art':
                query = project.query(f'SELECT * FROM open_ai.fine_art WHERE text="{text}";')
            elif style.name == 'street-art':
                query = project.query(f'SELECT * FROM open_ai.urban_art WHERE text="{text}";')
            elif style.name == 'abstract-art':
                query = project.query(f'SELECT * FROM open_ai.abstract WHERE text="{text}";')
            elif style.name == 'photography':
                query = project.query(f'SELECT * FROM open_ai.stock_photos WHERE text="{text}";')
            else:
                query = None
            if query is not None:
                ai_img = DataFrame.to_string(query.fetch())
                # Extract the image URL from ai_img using regular expressions
                url_pattern = r'(https?://\S+)'
                match = re.search(url_pattern, ai_img)
                if match:
                    image_url = match.group(1)
                else:
                    # Handle the case where no valid URL is found
                    image_url = None
            else:
                # Handle the case where the selected style is not recognized
                image_url = None
            
            if image_url:
                # Download the image from the URL
                response = requests.get(image_url)
                if response.status_code == 200:
                    img_temp = NamedTemporaryFile(delete=True)
                    img_temp.write(response.content)
                    img_temp.flush()

                    # Generate a random name for the image file
                    timestamp = str(int(time.time()))  # Get the current timestamp
                    random_str = ''.join(random.choices(string.ascii_lowercase, k=6))  # Generate a random string of length 6
                    image_filename = f'image_{timestamp}_{random_str}.jpg'

                    # Assign the downloaded image to the artwork model with the random name
                    artwork.image_url = image_url
                    artwork.image.save(image_filename, files.File(img_temp))
                    artwork.save()  # Save the artwork model again to update the image field

            return redirect(reverse('hugo'))
    else:
        form = ArtworkForm()

    template = 'add_hugo.html'
    context = {'form': form}

    return render(request, template, context)

def add_artwork_to_cart(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)

    # Call the add_to_cart view to add the artwork to the cart
    add_to_cart(request, artwork.id, quantity=1)

    return redirect('cart:view_cart') 