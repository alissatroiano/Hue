import os
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import HugoForm
from .models import Hugo
import openai
from django.conf import settings
from django.contrib import messages
import mindsdb_sdk
import pandas as pd
from pandas import DataFrame
email = os.environ["MINDSDB_EMAIL"]
password = os.environ["MINDSDB_PASSWORD"]


def hugo(request):
    """ A view to show all a user's hugos """
    hugos = Hugo.objects.all()
    image_url = None

    if request.GET:
        hugos = hugos.order_by('-created_at')
        image_url = request.GET['image_url']

    context = {
        'hugos': hugos,
        'image_url': image_url,
    }

    return render(request, 'hugo.html', context)


@login_required
def add_hugo(request):
    form = HugoForm()
    artwork = []
    if request.method == 'POST':
        # Retrieve the artwork description from the POST request
        text = request.POST.get('artwork_description')

        # Call your MindsDB/ChatGPT model to get the predictions
        mdb_server = mindsdb_sdk.connect('https://cloud.mindsdb.com', settings.MINDSDB_EMAIL, settings.MINDSDB_PASSWORD)
        project = mdb_server.get_project('open_ai')
        query = project.query(f'SELECT * FROM open_ai.art_model WHERE text="{text}";')
        print(query.fetch())
        artwork = DataFrame.to_dict(query.fetch(), orient='records')
        print(artwork)
    return render(request, 'add_hugo.html', {'form': form, 'artwork': artwork})

# @login_required
# def get_title_suggestions(request):
#     form = ArtworkForm()
#     predicted_titles = []
#     if request.method == 'POST':
#         # Retrieve the artwork description from the POST request
#         text = request.POST.get('text')

#         # Call your MindsDB/ChatGPT model to get the predictions
#         mdb_server = mindsdb_sdk.connect('https://cloud.mindsdb.com', settings.MINDSDB_EMAIL, settings.MINDSDB_PASSWORD)
#         project = mdb_server.get_project('open_ai')
#         query = project.query(f'SELECT * FROM open_ai.art WHERE artwork_description="{text}";')

#         predicted_titles = DataFrame.to_dict(query.fetch(), orient='records')
    
#     return render(request, 'shop/get_title_suggestions.html', {'predicted_titles': predicted_titles})
