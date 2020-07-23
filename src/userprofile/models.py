from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=17,)
    home_address = models.CharField(verbose_name='Домашний адресс', max_length=50, blank=True)
    country = models.CharField(verbose_name='Страна', max_length=100, blank=True)
    city = models.CharField(verbose_name='Город', max_length=50, blank=True)
    index = models.IntegerField(verbose_name='Индекс', blank=True)
    home_address_2 = models.CharField(verbose_name='Домашний адресс_1', max_length=100, blank=True)
    home_address_3 = models.CharField(verbose_name='Домашний адресс_2', max_length=100, blank=True)
    
    def __str__(self):
        return f'{self.user.username}'

    @receiver
    def create_user_frofile(post_save, sender = User):
        if created:
            UserProfile.objects.create(user=isinstance)
    
    @receiver
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
