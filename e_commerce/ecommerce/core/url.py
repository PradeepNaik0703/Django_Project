from django.urls import path
from . import views
from django.conf.urls.static import static
from ecommerce import settings

urlpatterns = [
    path("", views.store_veiw, name='store'),
    path("cart", views.cart_view, name='cart'),
    path("checkout", views.checkout_view, name='checkout')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)