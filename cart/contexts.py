from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from shop.models import Product


def cart_items_function(request):

	cart_items = []
	total= 0
	product_count = 0
	cart = request.session.get('cart', {})

	for item_id, quantity in cart.items():
		product = get_object_or_404(Product, pk=item_id)
		total += quantity * product.price
		product_count += quantity
		cart_items.append({
			'item_id': item_id,
			'quantity': quantity,
			'product': product,
		})

	if total < settings.PROMOTION_MINIMUM:
		promotion =  total * Decimal(settings.PROMOTION_PERCENTAGE / 100)
		promotion_delta = settings.PROMOTION_MINIMUM - total
	else:
		promotion = 0
		promotion_delta = 0

	grand_total = promotion + total 

	context = {
		'cart_items': cart_items,
		'total': total,
		'product_count': product_count,
		'promotion': promotion,
		'promotion_delta': promotion_delta,
		'promotion_minimum': settings.PROMOTION_MINIMUM,
		'promotion_percentage': settings.PROMOTION_PERCENTAGE,
		'grand_total': grand_total,
		}

	return context
