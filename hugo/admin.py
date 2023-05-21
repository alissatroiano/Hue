from django.contrib import admin
from django.conf import settings
from .models import userArtwork, Hugo

# Register your models here.

@admin.register(userArtwork)
class userArtworkAdmin(admin.ModelAdmin):
    fields = ('artwork', 'titles', 'predicted_titles')


@admin.register(Hugo)
class HugoAdmin(admin.ModelAdmin):
    fields = ('name', 'artwork_description', 'artwork', 'titles', 'predicted_titles')
    