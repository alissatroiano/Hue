from django.contrib import admin
from .models import ArtistInfo

# Register your models here.


@admin.register(ArtistInfo)
class ArtistInfoAdmin(admin.ModelAdmin):
    fields = ('artist', 'photo')
