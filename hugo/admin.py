from django.contrib import admin
from django.conf import settings
from .models import userArtwork, Hugo

# Register your models here.

@admin.register(userArtwork)
class userArtworkAdmin(admin.ModelAdmin):
    fields = ('artwork', 'titles', 'predicted_titles', 'user')


@admin.register(Hugo)
class HugoAdmin(admin.ModelAdmin):
    fields = ('name', 'user', 'artwork_description', 'artwork', 'image_url', 'genArt', 'titles', 'predicted_titles')
