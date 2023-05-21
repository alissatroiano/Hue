from urllib import request
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
# from .models import userArtwork, Hugo
from django.contrib.auth.models import User
# from .forms import userArtwork
# import mindsdb_sdk
import openai
# import pandas as pd
# from pandas import DataFrame
from django.shortcuts import render


# Create your views here.
@login_required
def hugo(request):
        response = openai.Image.create(
                prompt='cartoon of a siamese purple cat on a yellow background',
                n=1,
                size="1024x1024"
            )
        image_url = response['data'][0]['url']
        
        return render(request, 'hugo.html', {'image_url': image_url})

