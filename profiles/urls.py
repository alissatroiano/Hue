from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('edit_artwork/<int:artwork_id>/', views.edit_artwork, name='edit_artwork'),
    path('delete_artwork/<int:artwork_id>/', views.delete_artwork, name='delete_artwork'),
]
