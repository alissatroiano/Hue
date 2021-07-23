import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from shop.models import Product
from profiles.models import Profile

from decimal import Decimal
CURRENCY = settings.CURRENCY

import datetime
now = datetime.datetime.now()

class Order(models.Model):
    order_number = models.CharField(
        max_length=32, null=False, editable=False, unique=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name="orders")
    user_full_name = models.CharField(max_length=50, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=50, null=False, blank=False)
    street_address2 = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    special_discount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(
        null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _create_order_number(self):
        """
        This function uses UUID to generate unique order numbers for orders 
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.orderitems.aggregate(Sum('orderitem_total'))[
            'orderitem_total__sum'] or 0
        if self.order_total >= settings.PROMOTION_MINIMUM:
            self.special_discount = self.order_total * \
                Decimal(settings.PROMOTION_PERCENTAGE)
            self.grand_total = self.order_total - self.special_discount
        else:
            self.special_discount = 0
        self.grand_total = self.order_total - self.special_discount
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    """
    The OrderItem model stores data of the product and the amount of the product
    """
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    product_dimension = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=0)
    orderitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override save method to set update the order total with orderitem_total.
        """
        self.orderitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
