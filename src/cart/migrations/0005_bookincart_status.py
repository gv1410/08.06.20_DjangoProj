# Generated by Django 3.0.7 on 2020-07-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_bookincart_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookincart',
            name='status',
            field=models.CharField(choices=[('Ожидает подтверждения', 'Ожидает подтверждения'), ('Заказан', 'Заказан')], max_length=25, null=True, verbose_name='Статус'),
        ),
    ]