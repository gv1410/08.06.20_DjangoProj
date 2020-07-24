# Generated by Django 3.0.7 on 2020-07-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_bookincart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookincart',
            name='status',
            field=models.CharField(choices=[('Ожидает подтверждения', 'Ожидает подтверждения'), ('Заказан', 'Заказан')], default='Ожидает подтверждения', max_length=25, null=True, verbose_name='Статус'),
        ),
    ]