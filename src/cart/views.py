from django.shortcuts import render
from django.views.generic import UpdateView
from . import models
from testapp.models import Book
# Create your views here.


class AddBookToCart(UpdateView):
    models = models.BookInCart
    template_name = 'cart/add.html'
    fields = ('quantity',)

    def get_object(self):
        cart_pk = self.request.session.get('cart_pk', None)
        book_pk = self.request.GET.get('book_pk')
        book = Book.objects.get(pk=int(book_pk))
        user = self.request.user
        self.models.objects.get(pk=self.kwargs.get('pk'))
        #cart =
        cart, create = models.Cart.objects.get_or_create(
            pk = int(cart_pk),
            user = user,
            defaults={},
        )
        if create:
            cart_pk = self.request.session['cart_pk'] = cart.pk

        obj, create = self.models.objects.get_or_create(
            cart = cart,
            book = book,
            defaults={},
        )
        return obj 
