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


def hugo(request):
    artworks = Artwork.objects.all()
    styles = None

    # sort artwork by style if the user has selected that style
    if request.GET:
        if 'style' in request.GET:
            styles = request.GET['style'].split(',')
            artworks = artworks.filter(style__name__in=styles)
            styles = Style.objects.filter(name__in=styles)
    # display artwork from newest to oldest whe visiting the page
    artworks = artworks.order_by('-created_at')
    context = {
        'artworks': artworks,
        'styles': styles,
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
            
            # Query the respective model based on the selected style
            if style.name == 'pop art':
                query = project.query(f'SELECT * FROM open_ai.retro WHERE text="{text}";')
            elif style.name == 'digital-art':
                query = project.query(f'SELECT * FROM open_ai.digital_only WHERE text="{text}";')
            elif style.name == 'fine-art':
                query = project.query(f'SELECT * FROM open_ai.fine_art WHERE text="{text}";')
            else:
                # Handle the case where the selected style is not recognized
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
