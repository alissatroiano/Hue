from django.urls import path
from . import views

urlpatterns = [
    path('', views.hugo, name='hugo'),
    path('<artwork_id>', views.artwork_detail, name='artwork_detail'),
    path('add_hugo/', views.add_hugo, name='add_hugo'),  
    path('create_product', views.create_product, name='create_product'),
]
