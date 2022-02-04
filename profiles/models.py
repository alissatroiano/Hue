from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.conf import settings

from django_countries.fields import CountryField


class UserType(models.Model):
    """User type"""
    typename = models.CharField(verbose_name='User type',
                                max_length=150)

    def __str__(self):
        return f'{self.id} - {self.typename}'


USERTYPE_SELLER = 100
USERTYPE_BUYER = 200
USERTYPE_DEFAULT = USERTYPE_BUYER


class CustomUserManager(UserManager):
    """Manager for extended user model"""

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Extended user model"""

    class Meta(object):
        db_table = 'custom_user'

    # Use the created manager class
    objects = UserManager()

    # Have a user type in the model
    userType = models.ForeignKey(UserType,
                                 verbose_name='User type',
                                 null=True,
                                 blank=True,
                                 on_delete=models.PROTECT)

    def __str__(self):
        return self.username


class UserArtistProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, unique=True, db_index=True, related_name='product_seller', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    bio = models.TextField(max_length=500, blank=True, null=True)
    artist_website = models.URLField(blank=True)
    artist_twitter_handle = models.CharField(
        max_length=20, null=True, blank=True)
    artist_behance_handle = models.CharField(
        max_length=20, null=True, blank=True)
    artist_instagram_handle = models.CharField(
        max_length=20, null=True, blank=True)
    artist_email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to='avatars', default="avatar.jpg")

    def __str__(self):
        user = CustomUser.objects.get(pk=self.user_id)
        return f'{user.id} - {user.username} - {user.email} - {self.id} - {self.bio}'


@receiver(post_save, sender=CustomUser)
def create_or_update_artist_profile(sender, instance, created, **kwargs):
    """
    Creates a Profile instance for each User instance.
    """
    if created:
        UserArtistProfile.objects.create(user=instance)
        # Current users can simply save the profile.
    instance.userartistprofile.save()


class Profile(models.Model):
    """
    A user profile model for storing billing details & order history.
    """
    user = models.OneToOneField(
        CustomUser, unique=True, db_index=True, related_name='product_buyer', on_delete=models.CASCADE)
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
            avatar.avatar_thumbnail = File(open('media/avatar.jpg'))
            avatar.save()

    def __str__(self):
        user = CustomUser.objects.get(pk=self.user_id)
        return f'{user.id} - {user.username} - {user.email} - {self.id}'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates a Profile instance for each User instance.
    """
    if created:
        Profile.objects.create(user=instance)
        # Current users can simply save the profile.
    instance.profile.save()
