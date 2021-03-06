from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import * 
import datetime
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import os
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import BookInCart, Cart
from order.models import Order
from django.contrib.auth import authenticate, login
# Create your views here.

def test(request):
    #post_data = request.POST
    #name = request.POST.get('name')
    #description = request.POST.get('description')
    #obj = Genre(name = name, description = description)
    

    #form = CreateGenreForm()
    #form.save()
    genre = Genre.objects.all()
    books = Book.objects.all()

    login = request.user
    
        
    books_in_cart = BookInCart.objects.all()

    context = {'genre': genre, 'books': books, 'user': user, 'books_in_cart': books_in_cart} 
    return render(request, template_name='testapp/test.html', context= context)

def userdetail(request):
    login = request.user
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    books_in_cart = BookInCart.objects.all()
    context = {'login': login, 'first_name': first_name, 'last_name':last_name, 'email':email, 'books_in_cart': books_in_cart}
    return render(request, template_name='testapp/userdetail.html', context=context)
class CreateGenre(CreateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testapp/creategenre.html'
    success_url = '/listgenre'

class CreateBook(CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = 'testapp/createbook.html'
    success_url = '/listbook'

class UpdateGenre(UpdateView):
    model = Genre
    form_class = CreateGenreForm
    queryset = Genre.objects.all()
    template_name = 'testapp/creategenre.html'
    success_url = '/listgenre'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Genre, id=id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    
class ListGenre(ListView):
    model = Genre
    template_name = 'testapp/listgenre.html'

class DeleteGenre(DeleteView):
    model = Genre
    template_name = 'testapp/deletegenre.html'
    success_url = '/listgenre'

class UpdateBook(UpdateView):
    model = Book
    form_class = CreateBookForm
    queryset = Book.objects.all()
    template_name = 'testapp/createbook.html'
    success_url = '/listbook'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Book, id=id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ListBook(ListView):
    model = Book
    template_name = 'testapp/listbook.html'

    def get_context_data(self, **kwargs):
        key1 = self.request.GET.get('key1')
        c = super().get_context_data(**kwargs)
        c['key1'] = key1
        return c


class DeleteBook(DeleteView):
    model = Book
    template_name = 'testapp/deletebook.html'
    success_url = '/listbook'

class DetailBook(DetailView):
    model = Book
    template_name = 'testapp/detailbook.html'

class DetailGenre(DetailView):
    model = Genre
    template_name = 'testapp/detailgenre.html'

class HomepageList(ListView):
    model = Book
    template_name = 'testapp/homepage.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_list'] = Genre.objects.all()
        return context


def homepage(request):
    template = 'testapp/homepage.html'
    context = {}
    return render(request, template, context)
    
class CreateWriter(CreateView):
    model = Writer
    form_class = CreateWriterForm
    template_name = 'testapp/createwriter.html'
    success_url = '/listwriter'

class ListWriter(ListView):
    model = Writer
    template_name = 'testapp/listwriter.html'

class DetailWriter(DetailView):
    model = Writer
    template_name = 'testapp/detailwriter.html'


class UserLoginView(LoginView):
    template_name = 'testapp/login.html'
    form_class = AuthUserForm
    success_url = '/homepage'

    def get_success_url(self):
        return self.success_url

class UserRegistrView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'testapp/userregister.html'
    success_url = '/homepage'
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user = authenticate(
            username = username, 
            password = password, 
            )
        login(self.request, aut_user)
        return form_valid


class UserLogOutView(LogoutView):
    next_page = '/homepage'







