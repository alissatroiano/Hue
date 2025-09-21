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
from django.core.files.temp import NamedTemporaryFile
import requests
import pandas as pd
from pandas import DataFrame
import random
import string
from urllib.parse import quote
import base64
from openai import OpenAI
import time
from django.core.files.base import ContentFile

# Initialize OpenAI client with explicit API key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")
client = OpenAI(api_key=api_key)


@login_required
def create_image(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST)  # prompt, title etc.
        if form.is_valid():
            prompt = form.cleaned_data.get('artwork_description')
            result = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                response_format="b64_json"
            )

            image_base64 = result.data[0].b64_json
            image_bytes = base64.b64decode(image_base64)

            import time
            import random
            import string
            from PIL import Image
            import io
            
            # Convert PNG to JPG
            png_image = Image.open(io.BytesIO(image_bytes))
            rgb_image = png_image.convert('RGB')
            jpg_buffer = io.BytesIO()
            rgb_image.save(jpg_buffer, format='JPEG', quality=95)
            jpg_bytes = jpg_buffer.getvalue()
            
            # Create unique filename
            timestamp = int(time.time())
            random_suffix = ''.join(random.choices(string.ascii_lowercase, k=6))
            filename = f"image_{timestamp}_{random_suffix}.jpg"
            
            # Save artwork first
            artwork = form.save(commit=False)
            artwork.user = request.user
            artwork.save()
            
            # Then save the image
            artwork.image.save(
                filename,
                ContentFile(jpg_bytes),
                save=True
            )

            messages.success(request, 'Artwork created successfully!')
            return redirect('hugo')
    else:
        form = ArtworkForm()

    return render(request, 'create_image.html', {'form': form})

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