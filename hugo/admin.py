from django.contrib import admin
from django.conf import settings
from .models import Artwork

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    fields = [  
        'title', 'user', 'artwork_description', 'image_url', 'image'
    ]