# Generated by Django 3.0.7 on 2020-07-24 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20200724_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookincart',
            name='status',
            field=models.CharField(choices=[('Ожидает подтверждения', 'Ожидает подтверждения'), ('Заказан', 'Заказан')], default='Ожидает подтверждения', max_length=25, verbose_name='Статус'),
        ),
    ]
