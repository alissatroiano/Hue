from django.db import models
from django.conf import settings
from .managers import ProductManager
from django.utils import timezone

# https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/
now = timezone.now
CURRENCY = settings.CURRENCY

    # https://github.com/Code-Institute-Solutions/Boutique-Ado/blob/master/06-Products-Setup/Adding-The-Products/products/models.py
class Category(models.Model):
    # parent solution copied from https://www.youtube.com/watch?v=QIoUJ1PutV0
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


# https://christosstath10.medium.com/create-your-own-point-of-sale-c25f8b1ff93b
class Product(models.Model):
    sku = models.CharField(unique=True, max_length=254, null=True, blank=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=254, unique=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_details = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=10)
    final_price = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=10)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    qty = models.PositiveIntegerField(default=0)
    # https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    hue_manager = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        self.final_price = self.discount_price if self.discount_price > 0 else self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def display_final_price(self):
        return f'{CURRENCY} {self.final_price}'
    display_final_price.short_description = 'Price'
