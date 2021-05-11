from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'title', 'category', 'price', 'display_final_price', 'active', 'image']
    # Add list_selected_related so django will perform less queries on the database
    list_select_related = ['category']
    list_filter = ['active', 'category', 'price', 'created_at', 'deleted_at', 'discount_price']
    # Add search_fields so autocomplete will work in product admin 
    search_fields = ['title']
    list_per_page = 50
    fields = ['sku', 'active', 'title', 'image', 'category', 'price', 'discount_price', 'display_final_price']
    autocomplete_fields = ['category']
   # Add display_final_price to readonly_fields because it is a function not a db field
    readonly_fields = ['display_final_price']
