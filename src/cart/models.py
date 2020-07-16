from django.db import models
from django.contrib.auth import get_user_model
from testapp.models import Book

User = get_user_model()
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='carts',
    )
    def __str__(self):
        return f'Cart #{self.pk}'


class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='books',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='books_in_cart',
    )
    quantity = models.IntegerField(
        verbose_name='Qantity',
        default=1
    )
    def __str__(self):
        return f'Book #{self.book.pk} in cart #{self.cart.pk}'

    class Meta:
        unique_together = (('cart', 'book'),)

    
