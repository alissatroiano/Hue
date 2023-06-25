from django.contrib import admin
from django.conf import settings
from .models import Hugo, Artwork


# Register your models here.
@admin.register(Hugo)
class HugoAdmin(admin.ModelAdmin):
    fields = [
        'name', 'user', 'artwork_description', 'img_url', 'image'
    ]

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    fields = [  
        'title', 'user', 'artwork_description', 'image_url', 'image'
    ]