from django.urls import path
from .views import product_list, calculate_order
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('calculate_order/', calculate_order, name='calculate_order')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
