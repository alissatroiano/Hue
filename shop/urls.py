from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_all, name='shop'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]
