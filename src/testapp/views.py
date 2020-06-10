from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Genre, Book
from .forms import CreateGenreForm, CreateBookForm
import datetime
from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
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

    context = {'genre': genre, 'books': books}
    return render(request, template_name='testapp/test.html', context= context)


'''
class Test(TemplateView):
    template_name = 'testapp/test.html'
    
    def get_context_data(self, **kwargs):
        context = super(Test).get_context_data(**kwargs)
'''
class CreateGenre(CreateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = 'testapp/creategenre.html'
    success_url = '/test'

class CreateBook(CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = 'testapp/createbook.html'
    success_url = '/test'

#class GenreDetailView(DetailView):


class UpdateGenre(UpdateView):
    model = Genre
    form_class = CreateGenreForm
    queryset = Genre.objects.all()
    template_name = 'testapp/creategenre.html'
    success_url = '/test'

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
    success_url = '/test'
    