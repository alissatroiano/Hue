import os
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArtworkForm
from .models import Artwork
from django.conf import settings
from django.contrib import messages
import mindsdb_sdk
import pandas as pd
from pandas import DataFrame
email = os.environ["MINDSDB_EMAIL"]
password = os.environ["MINDSDB_PASSWORD"]


def hugo(request):
    """ A view to show all a user's hugos """
    hugo = Artwork.objects.all()
    image_url = None

    if request.GET:
        hugo = hugo.order_by('-created_at')
        image_url = request.GET['image_url']

    context = {
        'image_url': image_url,
    }

    return render(request, 'hugo.html', context)


@login_required
def add_hugo(request):
# A view to add a hugo to the database 
    if request.method == 'POST':
        # Retrieve the artwork description from the POST request
        text = request.POST.get('artwork_description')

        mdb_server = mindsdb_sdk.connect('https://cloud.mindsdb.com', settings.MINDSDB_EMAIL, settings.MINDSDB_PASSWORD)
        project = mdb_server.get_project('open_ai')
        query = project.query(f'SELECT * FROM open_ai.artwork WHERE text="{text}";')
        ai_img = query.fetch()
        print(ai_img)
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hugo')
    else:
        form = ArtworkForm()

    template = 'add_hugo.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
   