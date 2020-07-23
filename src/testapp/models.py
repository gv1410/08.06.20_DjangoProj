from django.db import models
from django.contrib.auth.models import User#get_user_model
#User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Writer(models.Model):
    name = models.CharField(verbose_name='ФИО Автора', max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра', max_length=100)
    description = models.TextField(verbose_name='Описание жанра', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):

    CATEGORY = (
        ('На складе', 'На складе'),
        ('Отсутствует на складе', 'Отсутствует на складе')
    )

    name = models.CharField(
        verbose_name='Название Книги', max_length=200
        )
    description = models.TextField(
        verbose_name='Описание Книги', null=True, blank=True
        )
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, verbose_name='Жанр Книги',
        )
    writer = models.ManyToManyField(
        Writer)
    created = models.DateField(
        verbose_name='Создано', auto_now=False, auto_now_add=True
        )
    updated = models.DateField(
        verbose_name='Изменено', auto_now=True, auto_now_add=False
        )
    book_image = models.ImageField(
        verbose_name='Изображение книги', upload_to='profile', null=True, blank=True 
        )
    price = models.FloatField(verbose_name='Цена', null=True)
    
    category = models.CharField(verbose_name='Статус', null=True, max_length=25, choices=CATEGORY)

    quantity_in_stok = models.IntegerField(verbose_name='Количество на складе', max_length=3)
    
    def __str__(self):
        return self.name

