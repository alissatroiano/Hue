from django.urls import path
from . import views

urlpatterns = [
    path('', views.hugo, name='hugo'),
    path('add_hugo/', views.add_hugo, name='add_hugo'),  
]
