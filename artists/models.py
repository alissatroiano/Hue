from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from django.contrib.auth.models import User

# Create your models here.


class ArtistInfo(models.Model):
    # user = models.OneToOneField(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    artist_twitter_handle = models.CharField(
        max_length=20, null=True, blank=True)
    artist_behance_handle = models.CharField(
        max_length=20, null=True, blank=True)
    artist_instagram_handle = models.CharField(
        max_length=20, null=True, blank=True)
    artist_email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to='avatars', default="avatar.jpg")

    def __str__(self):
        return self.name


# @receiver(post_save, sender=User)
# def create_or_update_artist_info(sender, instance, created, **kwargs):
#     """ Creates a ArtistProfile instance for each User instance."""
#     if created:
#         ArtistInfo.objects.create(user=instance)
#         # Current users can simply save the profile.
#     instance.artistinfo.save()
