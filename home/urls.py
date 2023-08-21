from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('page_not_found_view/', views.page_not_found_view, name='page_not_found_view')
]
