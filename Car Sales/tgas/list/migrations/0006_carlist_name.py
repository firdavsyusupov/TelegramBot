# Generated by Django 4.1.2 on 2022-10-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_carlist_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='name',
            field=models.TextField(default=1, verbose_name='Модель автомобиля'),
            preserve_default=False,
        ),
    ]