from django import forms
from .models import Genre, Book
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', 'description')

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_image', 'name', 'description','genre')

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user