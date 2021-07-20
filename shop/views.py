from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category

# Create your views here.
def shop_all(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query= None
    categories = None
    labels = None
    sort = None
    direction = None

    # https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/673a36fdd4bb2c09f8843c6ad8cb6ae4a60dda01/templates/includes/main-nav.html
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))
            if sortkey == 'category':
                sortkey = 'category__title'
            if sortkey == 'orientation':
                 sortkey = 'product__orientation'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__title__in=categories)
            categories = Category.objects.filter(title__in=categories)
            
        if 'people' in request.GET:
            peoples = request.GET['people'].split(',')
            categories = Category.filter(people__in=peoples)
            for i,l in enumerate(labels):
                [i] = Product.get_label(l)

        if 'label' in request.GET:
            labels = request.GET['label'].split(',')
            products = products.filter(label__in=labels)
            for i,l in enumerate(labels):
                labels[i] = Product.get_label(l)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('shop'))
            
            queries = Q(title__icontains=query) | Q(product_details__icontains=query) |  Q(label__icontains=query) | Q(category__title__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    print('The labels are:', labels)

    context = {
        'products': products,
        'search_term': query,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_labels': labels,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)
