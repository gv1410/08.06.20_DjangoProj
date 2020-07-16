from django.urls import path
from cart.views import AddBookToCart
from django.conf import settings
from django.conf.urls.static import static
app_name = 'cart'
urlpatterns = [
    path('add/', AddBookToCart.as_view(), name='add'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
