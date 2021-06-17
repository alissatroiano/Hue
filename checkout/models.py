import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from shop.models import Product
import datetime

from decimal import Decimal
CURRENCY = settings.CURRENCY
# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    billing_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now_add=True)
    tax_rate = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    hue_cart = models.TextField(
        null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _create_order_number(self):
        """
        This function uses UUID to generate unique order numbers for orders 
        """
        return uuid.uuid4().hex.upper()

    def update_grand_total(self):
    	"""
    	Update grand total each time a line item is added,
    	accounting for delivery costs.
    	"""
    	self.order_total = self.lineitems.aggregate(
    	    Sum('orderitem_total'))['orderitem_total__sum'] or 0
    	if self.order_total is not None:
    	    self.order_total = self.order_total * Decimal(settings.TAX_RATE / 100)
    	else:
    	    self.tax_rate = 0
    	self.grand_total = self.order_total * self.tax_rate
    	self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    """
    The OrderItem model stores data of the product and the amount of the product
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    product_dimension = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=0)
    orderitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.orderitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

