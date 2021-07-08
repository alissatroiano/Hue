from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from shop.models import Product


def cart_components(request):

	cart_items = []
	total= 0
	product_count = 0
	cart = request.session.get('cart', {})

	for item_id, item_data in cart.items():
		if isinstance(item_data, int):
			product = get_object_or_404(Product, pk=item_id)
			total += item_data * product.price
			product_count += item_data
			# print(quantity, product.price, product.final_price, total)
			cart_items.append({
				'item_id': item_id,
				'quantity': item_data,
				'product': product,
			})
		else:
			product = get_object_or_404(Product, pk=item_id)
			for dimension, quantity in item_data['items_by_dimension'].items():
				total += quantity * product.price
				product_count += quantity
				cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'dimension': dimension,
                })

	if total >= Decimal(settings.PROMOTION_MINIMUM):
		promotion = total * Decimal(settings.PROMOTION_PERCENTAGE)
		grand_total = total - promotion
	else:
		promotion = 0
	grand_total = total - promotion

	context = {
		'cart_items': cart_items,
		'total': total,
		'product_count': product_count,
		'promotion_minimum': settings.PROMOTION_MINIMUM,
		'promotion_percentage': settings.PROMOTION_PERCENTAGE,
		'grand_total': grand_total,
		}

	return context
