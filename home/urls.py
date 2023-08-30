from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import handler404
from .views import page_not_found_view

handler404 = page_not_found_view

urlpatterns = [
    path('', views.index, name='home'),
    path('faq/', views.faq, name='faq'),
    path('page_not_found_view/', views.page_not_found_view, name='page_not_found_view')
]
