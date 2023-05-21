from django.urls import path
from . import views

urlpatterns = [
    path('', views.hugo, name='hugo'),
]
