from django.shortcuts import render
from .models import Product

# Create your views here.

def product_details(request, product_id):

    product = get_object_or_404(product, pk=product_id)

    user = request.user
    product.set_flag(user)
    product.is_flagged(user)
    product.remove_flag(user)
  