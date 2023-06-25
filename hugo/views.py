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
    hugo = Hugo.objects.all()
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
        form = HugoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hugo')
    else:
        form = HugoForm()

    template = 'add_hugo.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
            

# @login_required
# def add_hugo(request):
#     form = HugoForm()
#     hugo = Hugo()
#     image_url= []
#     if request.method == 'POST':
#         # Retrieve the artwork description from the POST request
#         text = request.POST.get('artwork_description')

#         # Call your MindsDB/ChatGPT model to get the predictions
#         mdb_server = mindsdb_sdk.connect('https://cloud.mindsdb.com', settings.MINDSDB_EMAIL, settings.MINDSDB_PASSWORD)
#         project = mdb_server.get_project('open_ai')
#         query = project.query(f'SELECT * FROM open_ai.art_model WHERE text="{text}";')
#         print(query.fetch())
#         image_url = (query.fetch())
#         print(image_url)

#         form = HugoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             hugo = Hugo.objects.create(
#                 name=request.POST.get('name'),
#                 user=request.user,
#                 artwork_description=request.POST.get('artwork_description'),
#                 image_url=query.fetch()),            
#             hugo.save()
#             messages.success(request, 'Successfully added Hugo!')
#             return redirect('add_hugo')
    
#     return render(request, 'add_hugo.html', {'form': form, 'image_url': image_url})
