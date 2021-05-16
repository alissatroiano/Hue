# https://christosstath10.medium.com/create-your-own-point-of-sale-c25f8b1ff93b
"""
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_delete
import datetime
from product.models import Product

from decimal import Decimal
CURRENCY = settings.CURRENCY


class ProductManager(models.Manager):


def active(self):
    return self.filter(active=True)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    billing_address = models.TextField()
    products = models.ManyToManyField(OrderItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=6, decimal_places=2) 


class Order(models.Model):
    title = models.CharField(blank=True, max_length=150)
    timestamp = models.DateField(auto_now_add=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount_price = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    final_price = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    is_paid = models.BooleanField(default=True)
    objects = models.Manager()
    browser = ProductManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ['-date']


def save(self, *args, **kwargs):
    order_items = self.order_items.all()
    # aggregate and Sum calculate price on DB
    self.price = order_items.aggregate(Sum('total_price'))[
        'total_price__sum']
    if order_items.exists()
    # Set else condition to zero so the app doesn't brake if the queryset is empty
    else 0.00
    # Use decimal here to ensure both values are on same format
    self.final_price = Decimal(self.price) - Decimal(self.discount)
    super().save(*args, **kwargs)

def __str__(self):
    return self.title if self.title else 'New Order'

def get_edit_url(self):
    return reverse('update_order', kwargs={'pk': self.id})

def get_delete_url(self):
    return reverse('delete_order', kwargs={'pk': self.id})

def display_final_price(self):
    return f'{self.final_price} {CURRENCY}'

def display_discount(self):
    return f'{self.discount} {CURRENCY}'

def display_price(self):
    return f'{self.price} {CURRENCY}'

@staticmethod
def filter_data(request, queryset):
    search_name = request.GET.get('search_name', None)
    date_start = request.GET.get('date_start', None)
    date_end = request.GET.get('date_end', None)
    queryset = queryset.filter(
        title__contains=search_name) if search_name else queryset
    if date_end and date_start and date_end >= date_start:
        date_start = datetime.datetime.strptime(
            date_start, '%m/%d/%Y').strftime('%Y-%m-%d')
        date_end = datetime.datetime.strptime(
            date_end, '%m/%d/%Y').strftime('%Y-%m-%d')
        print(date_start, date_end)
        queryset = queryset.filter(date__range=[date_start, date_end])
    return queryset


class Meta:
    ordering = ['-date']

def save(self, *args, **kwargs):
    order_items = self.order_items.all()
    self.value = order_items.aggregate(Sum('total_price'))['total_price__sum'] if order_items.exists() else 0.00
    self.final_value = Decimal(self.value) - Decimal(self.discount)
    super().save(*args, **kwargs)


# OrderItem stores data of the product and the amount of the product
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    qty = models.PositiveIntegerField(default=1)

def __str__(self):
    return f'{self.product.title}'

def save(self,  *args, **kwargs):
    self.final_price = self.discount_price if self.discount_price > 0 else self.price
    self.total_price = Decimal(self.qty) * Decimal(self.final_price)
    super().save(*args, **kwargs)
    self.order.save()

def display_final_price(self):
    return f'{self.final_price} {CURRENCY}'

def display_discount(self):
    return f'{self.discount_price} {CURRENCY}'

def display_price(self):
    return f'{self.price} {CURRENCY}'

@receiver(post_delete, sender=OrderItem)
def delete_order_item(sender, instance, **kwargs):
    product = instance.product
    product.qty += instance.qty
    product.save()
    instance.order.save()
    """

