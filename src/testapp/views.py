from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre, Book
from .forms import CreateGenreForm, CreateBookForm
import datetime
from django.views.generic import TemplateView
from django.views.generic import CreateView
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