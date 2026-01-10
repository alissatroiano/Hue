from django.contrib import admin
from .models import Artwork, Style

@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    fields = [  
        'title', 'user', 'artwork_description', 'image_url', 'image', 'style', 'is_downloadable', 'is_public', 'for_sale'
    ]