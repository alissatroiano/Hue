from django.db import models
from django.contrib.auth.models import User

class Style(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Styles'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

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
    style = models.ForeignKey('Style', null=True, blank=True,on_delete=models.SET_NULL)
    is_public = models.BooleanField(default=False)
    is_downloadable = models.BooleanField(default=False)
    for_sale = models.BooleanField(default=False)
    price = models.DecimalField(
    decimal_places=2, max_digits=8, null=False, default=0)
    in_import_queue = models.BooleanField(default=False)


    def get_style(s):
        """
        Return artworks that have a style
        """
        return dict((artwork.id, artwork) for artwork in Artwork.objects.filter(style=s)
                    .order_by('title'))
    
    def get_style_artworks(x):
         return dict(Artwork.objects.filter(style=x).order_by('title'))

    class Meta:
        verbose_name_plural = 'artworks'

    def save(self, *args, **kwargs):
             super().save(*args, **kwargs)

    def __str__(self):
        return self.title
