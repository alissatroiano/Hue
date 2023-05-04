from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_all, name='shop'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('get_title_suggestions/', views.get_title_suggestions, name='get_title_suggestions'),
    path('delete/<int:product_id>/',
         views.delete_product,
         name='delete_product'),
]
