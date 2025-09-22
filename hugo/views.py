import os, random, string, time, re, requests
from django.core import files
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .forms import ArtworkForm
from .models import Artwork, Style
from django.conf import settings
from django.contrib import messages
from django.core.files.temp import NamedTemporaryFile
import pandas as pd
from pandas import DataFrame
import random
import string
from urllib.parse import quote
import base64

from tempfile import NamedTemporaryFile
from urllib.parse import quote

from django.core import files
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse

from .forms import ArtworkForm
from openai import OpenAI

import time
from django.core.files.base import ContentFile

# Initialize OpenAI client with explicit API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@login_required
def create_image(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                artwork = form.save(commit=False)
                artwork.user = request.user
                artwork.save()
                
                style = artwork.style
                text = artwork.artwork_description
                
                # Define style-specific prompts
                style_prompts = {
                    'pop-art': f'A pop art style painting of {text}',
                    'digital-art': f'A digital art painting of {text}',
                    'fine-art': f'A fine art classical painting of {text}',
                    'street-art': f'A street art graffiti style painting of {text}',
                    'abstract-art': f'An abstract art painting of {text}',
                    'photography': f'A photographic style image of {text}'
                }
                
                prompt = style_prompts.get(style.name, text) if style else text
                
                # Generate image with OpenAI
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size="1024x1024",
                    response_format="b64_json"
                )
                
                b64_image = response.data[0].b64_json
                img_bytes = base64.b64decode(b64_image)
                
                # Generate filename
                timestamp = str(int(time.time()))
                random_str = ''.join(random.choices(string.ascii_lowercase, k=6))
                image_filename = f'image_{timestamp}_{random_str}.jpg'
                
                # Save image
                artwork.image.save(image_filename, ContentFile(img_bytes))
                artwork.save()
                
                return redirect(reverse('hugo'))
        except Exception as e:
            if 'artwork' in locals():
                artwork.delete()
            return render(request, 'runtime_error_template.html', {'error_message': str(e)})
    else:
        form = ArtworkForm()

    template = 'create_image.html'
    context = {'form': form}
    return render(request, template, context)

def hugo(request):
    """ A view to show the AI art gallery """
    artworks = Artwork.objects.filter(is_public=True, image__isnull=False).exclude(image='').order_by('-created_at')
    
    context = {
        'artworks': artworks,
    }
    
    return render(request, 'hugo.html', context)

def artwork_detail(request, artwork_id):
    """ A view to render a page for individual artwork and artwork details """
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artwork_detail.html', context)

# send image requests to Open AI endpoint https://api.openai.com/v1/images/generations

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.user = request.user
            artwork.save()
            messages.success(request, 'Artwork created successfully!')
            return redirect('hugo')
    else:
        form = ArtworkForm()

    return render(request, 'create_image.html', {'form': form})