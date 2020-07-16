from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
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

    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=17,)
    home_address = models.CharField(verbose_name='Домашний адресс', max_length=50, blank=True)
    country = models.CharField(verbose_name='Страна', max_length=100, blank=True)
    city = models.CharField(verbose_name='Город', max_length=50, blank=True)
    index = models.IntegerField(verbose_name='Индекс', blank=True)
    home_address_2 = models.CharField(verbose_name='Домашний адресс_1', max_length=100, blank=True)
    home_address_3 = models.CharField(verbose_name='Домашний адресс_2', max_length=100, blank=True)
    
    def __str__(self):
        return f'{self.user.username}'

class Order(models.Model):
    STATUS = (
        ('В ожидании', 'В ожидании'),
        ('Недоступен для заказа', 'Недоступен для заказа'),
        ('Доставлен', 'Доставлен')
    )

    customer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказ')
    status = models.CharField(max_length=200, null=True, choices=STATUS)