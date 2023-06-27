from django.db import models
from django.contrib.auth.models import User

class Artwork(models.Model):
    id = models.AutoField(primary_key=True)
    artwork_description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=254, unique=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='userz', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'artworks'

    def save(self, *args, **kwargs):
             super().save(*args, **kwargs)

    def __str__(self):
        return self.title
