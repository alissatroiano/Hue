from nntplib import ArticleInfo
from django.db import models
from django.dispatch import receiver

from django.contrib.auth.models import User

# Create your models here.


class ArtistInfo(models.Model):
    artist = models.OneToOneField(User, on_delete=models.CASCADE)
    artist_twitter_handle = models.CharField(
        max_length=20, null=True, blank=True)
    artist_behance_handle = models.CharField(
        max_length=20, null=True, blank=True)
    artist_instagram_handle = models.CharField(
        max_length=20, null=True, blank=True)
    artist_email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to='avatars', default="avatar.jpg")

    def create_default_photo(self):
        if not self.photo_set.all():
            photo = profile.photo_set.create(profile=self.__class__)
            photo.photo = File(open('media/photo.jpg'))
            photo.photo_thumbnail = File(open('media/photo.jpg'))
            photo.save()

    def __str__(self):
        return self.artist.username


# @receiver(post_save, sender=User)
# def create_or_update_artist_profile(sender, instance, created, **kwargs):
#     """ Creates a ArtistProfile instance for each User instance."""
#     if created:
#         ArticleInfo.objects.create(user=instance)
#         # Current users can simply save the profile.
#     instance.artistprofile.save()
