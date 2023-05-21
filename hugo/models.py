from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class userArtwork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ImageField(upload_to='artworks', blank=True, null=True)
    titles = models.TextField(blank=True)
    predicted_titles = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.artwork.name


class Hugo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, default='')
    artwork_description = models.TextField(blank=True)
    artwork = models.ImageField(upload_to='artworks', blank=True, null=True)
    titles = models.TextField(blank=True)
    predicted_titles = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.artwork.name