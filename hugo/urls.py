from django.urls import path
from . import views

urlpatterns = [
    path('', views.hugo, name='hugo'),
    path('<artwork_id>', views.artwork_detail, name='artwork_detail'),
    path('create_image/', views.create_image, name='create_image')
    ]
