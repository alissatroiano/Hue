from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from home.views import page_not_found_view

re_path = page_not_found_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('page_not_found_view/', page_not_found_view, name='page_not_found_view'),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('hugo/', include('hugo.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    static('django.views.static', (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
)