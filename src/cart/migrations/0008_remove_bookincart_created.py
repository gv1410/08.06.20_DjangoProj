# Generated by Django 3.0.7 on 2020-07-24 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20200724_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookincart',
            name='created',
        ),
    ]
