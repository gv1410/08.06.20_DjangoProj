from django.urls import path
from cart.views import AddBookToCart, CartDetailView, ProductInCartDeleteView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'cart'
urlpatterns = [
    path('add/', AddBookToCart.as_view(), name='add'),
    path('cart/',CartDetailView.as_view(), name='cart'),
    path('delete/<int:pk>',ProductInCartDeleteView.as_view(), name='delete'),
]
