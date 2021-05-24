from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


# Create your views here.
def shop_all(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query= None

    # https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/673a36fdd4bb2c09f8843c6ad8cb6ae4a60dda01/templates/includes/main-nav.html
    if request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('shop'))
    
        queries = Q(title__icontains=query) | Q(product_details__icontains=query)
        products = products.filter(queries, autocomplete_fields = ['title'])


    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)
