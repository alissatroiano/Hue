from django.conf import settings

def cart_items_function(request):

	cart_items = []
	total= 0
	product_count = 0
	cart = request.session.get('bag', {})

	context = {}

	return context