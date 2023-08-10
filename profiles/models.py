from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Profile(models.Model):
    """
    A user profile model for storing billing details & order history.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Select Country', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', default="avatar.jpg")

    def create_default_avatar(self):
        if not self.avatar_set.all():
            avatar = profile.avatar_set.create(profile=self.__class__)
            avatar.avatar = File(open('media/avatar.jpg'))
            avatar.avatar_thumbnail = File(open('media/static/images/profile-card-bg.jpg'))
            avatar.save()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates a Profile instance for each User instance.
    """
    if created:
        Profile.objects.create(user=instance)
        # Current users can simply save the profile.
    instance.profile.save()
