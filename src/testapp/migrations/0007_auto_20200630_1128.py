# Generated by Django 3.0.7 on 2020-06-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20200630_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='writer',
            field=models.ManyToManyField(blank=True, related_name='books', to='testapp.Writer'),
        ),
    ]