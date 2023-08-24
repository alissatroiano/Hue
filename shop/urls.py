from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_all, name='shop'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('<artwork_id>', views.artwork_detail, name='artwork_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product,
         name='delete_product'),
    path('import_artwork/', views.import_artwork_to_store, name='import_artwork_to_store'),
]
