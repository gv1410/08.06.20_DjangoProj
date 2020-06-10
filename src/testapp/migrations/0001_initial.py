# Generated by Django 3.0.7 on 2020-06-07 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название жанра')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание жанра')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название Книги')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание Книги')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateField(auto_now=True, verbose_name='Изменено')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testapp.Genre', verbose_name='Жанр Книги')),
            ],
        ),
    ]