from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from shop.models import Product


def cart_components(request):

	cart_items = []
	total= 0
	product_count = 0
	cart = request.session.get('cart', {})

	for item_id, quantity in cart.items():
		product = get_object_or_404(Product, pk=item_id)
		total += quantity * product.price
		product_count += quantity
		print(quantity, product.price, product.final_price, total)
		cart_items.append({
            'item_id': item_id,
            'total': total,
            'quantity': quantity,
            'product': product,
        })


	print('The total is', total)

	if total >= Decimal(settings.PROMOTION_MINIMUM):
		promotion = Decimal(settings.PROMOTION_PERCENTAGE)
		grand_total = total * Decimal(settings.PROMOTION_PERCENTAGE)
	else:
		promotion = 0
		grand_total = total

	context = {
		'cart_items': cart_items,
		'total': total,
		'product_count': product_count,
		'promotion_minimum': settings.PROMOTION_MINIMUM,
		'promotion_percentage': settings.PROMOTION_PERCENTAGE,
		'grand_total': grand_total,
		}

	print(context)
	print('The grand total is', grand_total)


	return context
