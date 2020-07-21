from django.shortcuts import render
from django.views.generic import UpdateView
from cart.models import Cart, BookInCart
from testapp.models import Book
from .models import Order
from django.urls import reverse_lazy
# Create your views here.

class CreateOrder(UpdateView):
    model = Order
    template_name = 'order/create.html'
    fields = ('delivery_address', 'contact_phone', )
    success_url = reverse_lazy('listbook')

    def get_object(self, *args, **kwargs):
    
        #self.request.user
        cart_pk = self.request.session.get('cart_pk')
        if cart_pk:
            cart = Cart.objects.get(pk=cart_pk)
            try:
                order_pk = cart.order.pk
            except:
                order_pk  = None

        obj, create = self.model.objects.get_or_create(
            pk = order_pk,
            defaults = {
                'cart': cart,
                'status': False,
                'delivery_address': 'Пожалуйста заполните строку!',
                'contact_phone': 'Пожалуйста заполните строку!',
            }
        )
        return obj
    
    def get_success_url(self):
        url = super().get_success_url()
        self.object.status = True
        
        
        for i in self.object.cart.books.all():
            b = Book.objects.get(name = i.book.name)
            i.book.quantity_in_stok = (i.book.quantity_in_stok - i.quantity)
            i.book.quantity_in_stok
            b.quantity_in_stok = i.book.quantity_in_stok
            b.save()

        
        
        self.object.save()
        del(self.request.session['cart_pk'])
        return url