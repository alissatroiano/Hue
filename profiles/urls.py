from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('artworkGenerated/', views.artworkGenerated, name='artworkGenerated'),
    path('user_profile/<str:username>/', views.user_profile, name='user_profile'),
]
