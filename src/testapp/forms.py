from django import forms
from .models import Genre, Book

class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', 'description')

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_image', 'name', 'description','genre')
