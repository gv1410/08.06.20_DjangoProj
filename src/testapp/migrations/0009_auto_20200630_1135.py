# Generated by Django 3.0.7 on 2020-06-30 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_auto_20200630_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testapp.Genre', verbose_name='Жанр Книги'),
        ),
    ]
