from django.db import models
from django.conf import settings
from .managers import ProductManager
from django.utils import timezone
from model_utils import Choices
from decimal import Decimal


# https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/
now = timezone.now
CURRENCY = settings.CURRENCY

ORIENTATION = (
        ('3','Portrait'),
        ('4', 'Landscape'),
        ('5', 'Square'),
)

LABEL = (
        ('1','With People'),
        ('2', 'Without People'),
)

    # https://github.com/Code-Institute-Solutions/Boutique-Ado/blob/master/06-Products-Setup/Adding-The-Products/products/models.py
class Category(models.Model):

    class Meta:
        unique_together = ('title', 'parent',) 
        verbose_name_plural = 'Categories'
    
    # parent solution copied from https://www.youtube.com/watch?v=QIoUJ1PutV0
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return  ' -> ' .join(full_path[::-1])
    
    def get_friendly_name(self):
        return self.friendly_name

# https://christosstath10.medium.com/create-your-own-point-of-sale-c25f8b1ff93b
class Product(models.Model):
    """
    The Product Model contains data for all shop products
    """
    sku = models.CharField(unique=True, max_length=254, null=True, blank=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=254, unique=True)
    orientation = models.CharField(choices=ORIENTATION, max_length=254, default='3')
    label = models.CharField(max_length=254, choices=LABEL, default='1')
    has_dimensions = models.BooleanField(default=False, null=True, blank=True)
    medium = models.CharField(max_length=254, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(
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
    
    def get_orientation(o):
        return dict(ORIENTATION).get(o)
    
    def get_category_list(self):
        """
        A method to fetch all sub/parent categories
        """
        k = self.category
        

    class Meta:
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
