from django.db import models


class ProductManager(models.Manager):
# Create the active query to get only the products we want to show (https://christosstath10.medium.com/create-your-own-point-of-sale-c25f8b1ff93b)
    def active(self):
        return self.filter(active=True)
# Create the have_qty query to filter active items
    def have_qty(self):
        return self.active().filter(qty__gte=1)
