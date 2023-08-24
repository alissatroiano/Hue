from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from hugo.models import Artwork
from django.contrib.auth.models import User
from profiles.views import add_artwork_to_store

from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm, EditProductForm
# import mindsdb config from settings.py
from django.conf import settings
import mindsdb_sdk
import pandas as pd
from pandas import DataFrame


from django.shortcuts import render

mdb_server = mindsdb_sdk.connect(settings.MINDSDB_HOST, settings.MINDSDB_EMAIL, settings.MINDSDB_PASSWORD)
project = mdb_server.get_project('mindsdb')


@login_required
def import_artwork_to_store(request):
    # Retrieve all artwork items
    artwork_items = Artwork.objects.filter(for_sale=True)

    for artwork in artwork_items:
        # Check if a product with the same title already exists
        if not Product.objects.filter(title=artwork.title).exists():
            # Create a new Product instance using data from artwork
            product = Product(
                title=artwork.title,
                price=artwork.price,
                image=artwork.image,
                created_at=artwork.created_at,
                user = artwork.user,
                style = artwork.style,
                artwork_description = artwork.artwork_description,)
            product.save()

    return redirect('shop')  # Redirect to the shop or another page


def shop_all(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    has_artwork_for_import = False
    if request.user.is_authenticated:
            has_artwork_for_import = Artwork.objects.filter(user=request.user, for_sale=True).exists()
    artwork_items = Artwork.objects.filter(for_sale=True)
    query = None
    categories = None
    current_sorting = None
    parents = None
    labels = None
    orientations = None
    sort = None
    direction = None

    # https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/673a36fdd4bb2c09f8843c6ad8cb6ae4a60dda01/templates/includes/main-nav.html

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            sortkey = 'lower_title'
            products = products.annotate(lower_title=Lower('title'))
            if sortkey == 'category':
                sortkey = 'category__title'
            if sortkey == 'parent':
                sortkey == 'product__parent'
                products = products.annotate(product_parent=Lower('parent'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                else:
                    sortkey = f'{sortkey}'
            current_sorting = f'{sort}_{direction}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__title__in=categories)
            categories = Category.objects.filter(title__in=categories)

        if 'parent' in request.GET:
            parents = request.GET['parent'].split(',')
            products = products.filter(parent__title__in=parents)
            categories = Category.objects.filter(parents__title__in=parents)

        if 'label' in request.GET:
            labels = request.GET['label'].split(',')
            products = products.filter(label__in=labels)
            for i, l in enumerate(labels):
                labels[i] = Product.get_label(l)

        if 'orientation' in request.GET:
            orientations = request.GET['orientation'].split(',')
            products = Product.objects.filter(orientation__in=orientations)
            for i, o in enumerate(orientations):
                orientations[i] = Product.get_orientation(o)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('shop'))

            queries = Q(title__icontains=query) | Q(label__icontains=query) | Q(orientation__icontains=query) | Q(
                category__title__icontains=query) | Q(parent__title__icontains=query) | Q(medium__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_labels': labels,
        'current_orientation': orientations,
        'has_artwork_for_import': has_artwork_for_import,
        'artwork_items': artwork_items,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)


def artwork_detail(request, artwork_id):
    """ A view to show individual artwork details """

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'hugo/artwork_detail.html', context)


@login_required
def add_product(request):
    """ A view so shop manager can add new products """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('shop'))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ A view so shop manager can edit existing products """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = EditProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'shop/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ A view so shop manager can delete existing products """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('shop'))
