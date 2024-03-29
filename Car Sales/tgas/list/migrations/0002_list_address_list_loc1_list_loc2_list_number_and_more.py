# Generated by Django 4.1.2 on 2022-10-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='address',
            field=models.TextField(default='Tashkent', verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='list',
            name='loc1',
            field=models.TextField(default=1, verbose_name='Локация-1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='loc2',
            field=models.TextField(default=1, verbose_name='Локация-2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='number',
            field=models.TextField(default=1, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.TextField(verbose_name='Наименования диллерского центра'),
        ),
    ]
