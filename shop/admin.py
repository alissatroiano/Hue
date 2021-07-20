from django.contrib import admin
from django.conf import settings
from .models import Category, Product
from django.utils import timezone

# https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/
now = timezone.now
CURRENCY = settings.CURRENCY


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'sku', 
        'title', 
        'active',
        'category', 
        'price',   
        'image']
    # Add list_selected_related so django will perform less queries on the database
    list_select_related = ['category']
    list_filter = ['active', 'category', 'price', 'created_at', 'deleted_at']
    # Add search_fields so autocomplete will work in product admin 
    search_fields = ['title']
    list_per_page = 50
    fields = [
        'sku',
        'title',
        'active', 
        'medium', 
        'image', 
        'category', 
        'price', 
        'orientation', 
        'has_dimensions'
    ]
    autocomplete_fields = ['category']
   # Add display_final_price to readonly_fields because it is a function not a db field
    readonly_fields = ['active']

    ordering = ('sku',)
