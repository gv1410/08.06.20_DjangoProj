from django.db import models

# Create your models here.

class Genre(models.Model):
    # pk PK + autoincrement not null
    name = models.CharField(verbose_name='Название жанра', max_length=100)
    description = models.TextField(verbose_name='Описание жанра', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(verbose_name='Название Книги', max_length=200)
    description = models.TextField(verbose_name='Описание Книги', null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name='Жанр Книги')
    created = models.DateField(verbose_name='Создано', auto_now=False, auto_now_add=True)
    updated = models.DateField(verbose_name='Изменено', auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name
