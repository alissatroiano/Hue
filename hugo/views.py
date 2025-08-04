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
client = OpenAI()
import time
# import openAI for Dalle use
request = "https://api.openai.com/v1/images/generations" 

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

# send image requests to Open AI endpoint https://api.openai.com/v1/images/generations

@login_required
def create_image(request):
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