import os
import re
from django.core import files
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArtworkForm
from .models import Artwork
from django.conf import settings
from django.contrib import messages
import mindsdb_sdk
from django.core.files.temp import NamedTemporaryFile
import requests
import openai
import pandas as pd
from pandas import DataFrame
email = os.environ["MINDSDB_EMAIL"]
password = os.environ["MINDSDB_PASSWORD"]


def hugo(request):
    """ A view to show all a user's hugos """
    artworks = Artwork.objects.all()
    image_url = None

    context = {
        'artworks': artworks,
    }

    return render(request, 'hugo.html', context)


def artwork_detail(request, artwork_id):
    """ A view to show individual product details """

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artwork_detail.html', context)


@login_required
def add_hugo(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        text = request.POST.get('artwork_description')
        
        mdb_server = mindsdb_sdk.connect('https://cloud.mindsdb.com', settings.MINDSDB_EMAIL, settings.MINDSDB_PASSWORD)
        project = mdb_server.get_project('open_ai')
        query = project.query(f'SELECT * FROM open_ai.beta_test WHERE text="{text}";')
        ai_img = DataFrame.to_string(query.fetch())

        # Extract the image URL from ai_img using regular expressions
        url_pattern = r'(https?://\S+)'
        match = re.search(url_pattern, ai_img)
        if match:
            image_url = match.group(1)
        else:
            # Handle the case where no valid URL is found
            image_url = None

        # Save the image_url from the query to the Artwork model as image_url
        if form.is_valid() and image_url:
            artwork = form.save(commit=False)
            
            # Download the image from the URL
            response = requests.get(image_url)
            if response.status_code == 200:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.content)
                img_temp.flush()

                # Assign the downloaded image to the artwork model
                artwork.image_url = image_url
                artwork.image.save(f'image.jpg', files.File(img_temp))

            artwork.save()
            form.save()

            return redirect(reverse('hugo'))
    else:
        form = ArtworkForm()

    template = 'add_hugo.html'
    context = {'form': form}

    return render(request, template, context)
