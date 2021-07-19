from django.db import models
from django.conf import settings
from .managers import ProductManager
from django.utils import timezone
from model_utils import Choices
from decimal import Decimal


# https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/
now = timezone.now
CURRENCY = settings.CURRENCY

ORIENTATIONS = (
        ('Portrait','Portrait'),
        ('Landscape', 'Landscape'),
        ('Square', 'Square'),
)
LABEL = (
        ('SL', 'Sale'),
        ('CL', 'Clearance'),
        ('NP', 'No Promotion'),
)

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
    """
    The Product Model contains data for all shop products
    """
    sku = models.CharField(unique=True, max_length=254, null=True, blank=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=254, unique=True)
    orientation = models.CharField(choices=ORIENTATIONS, max_length=254, default='Portrait')
    has_dimensions = models.BooleanField(default=False, null=True, blank=True)
    label = models.CharField(choices=LABEL, max_length=2, default='NP')
    medium = models.CharField(max_length=254, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_details = models.TextField()
    price = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=8)
    discount_price = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=8)
    final_price = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=8)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, )
    qty = models.PositiveIntegerField(default=0)
    # https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    product_manager = ProductManager()

    def get_label(l):
        return dict(LABEL).get(l)

    class Meta:
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        self.discount_price = self.price if self.discount_price > 0 else self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def display_final_price(self):
        if self.label == "SL":
            sale_discount = 0.75
            self.discount_price = self.price * Decimal(sale_discount)
            return '${:,.2f}'.format(self.discount_price)
        elif self.label == 'CL':
            clearance_discount = 0.25
            self.discount_price = self.price * Decimal(clearance_discount)
            return '${:,.2f}'.format(self.discount_price)
        else:
            self.price = self.price
        return f'{CURRENCY} {self.discount_price}'
    display_final_price.short_description = 'Display Final Price'

