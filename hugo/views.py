import os
from django.shortcuts import render, redirect, reverse, get_object_or_404
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
        text = request.POST.get('artwork_description')
        response = openai.Image.create(
            prompt=text,
            n=1,
            size="1024x1024"
        )
        artwork = response['data'][0]['url']
        print(artwork)
        form = HugoForm(request.POST, request.FILES)
        if form.is_valid():
            hugo = Hugo.objects.create(
                name=request.POST.get('name'),
                user=request.user,
                artwork_description=request.POST.get('artwork_description'),
                artwork=request.POST.get('artwork'),
                image_url=artwork,
                titles=request.POST.get('titles'),
                predicted_titles=request.POST.get('predicted_titles'),
            )
            hugo.user = request.user
            hugo.save()
            messages.success(request, 'Successfully added Hugo!')
            return redirect('add_hugo')

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
