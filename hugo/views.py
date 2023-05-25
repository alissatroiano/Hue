import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import HugoForm
from .models import Hugo
import openai
# import mindsdb config from settings.py
from django.conf import settings
from django.contrib import messages
# import mindsdb_sdk
import pandas as pd
from pandas import DataFrame


def hugo(request):
    """ A view to show all a user's hugos """

    hugos = Hugo.objects.all()

    context = {
        'hugos': hugos,
    }

    return render(request, 'hugo.html', context)


@login_required
def add_hugo(request):
    form = HugoForm()
    files = os.listdir('artworks')
    full_path = [os.path.join('artworks', i) for i in files]
    hugo = Hugo.objects.all()
    artwork = []
    if request.method == 'POST':
        form = HugoForm(request.POST)
        artwork_description = request.POST.get('artwork_description')
        if form.is_valid():
            artwork_description = request.POST.get('artwork_description')
            response = openai.Image.create(
                prompt=artwork_description,
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            return image_url

    return render(request, 'add_hugo.html', {'form': form})


@login_required
def get_title_suggestions(request):
    form = ArtworkForm()
    predicted_titles = []
    if request.method == 'POST':
        # Retrieve the artwork description from the POST request
        text = request.POST.get('text')

        # Call your MindsDB/ChatGPT model to get the predictions
        mdb_server = mindsdb_sdk.connect('https://cloud.mindsdb.com', settings.MINDSDB_EMAIL, settings.MINDSDB_PASSWORD)
        project = mdb_server.get_project('open_ai')
        query = project.query(f'SELECT * FROM open_ai.art WHERE artwork_description="{text}";')

        predicted_titles = DataFrame.to_dict(query.fetch(), orient='records')
    
    return render(request, 'shop/get_title_suggestions.html', {'predicted_titles': predicted_titles})
