# Generated by Django 4.1.2 on 2022-10-21 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField(unique=True, verbose_name='ID пользователя в соц сети')),
                ('name', models.TextField(verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Заявка')),
                ('region', models.TextField(blank=True, null=True, verbose_name='Регион')),
                ('dealer_company', models.TextField(blank=True, null=True, verbose_name='Дилерское предприятие')),
                ('type_car', models.TextField(blank=True, null=True, verbose_name='Тип машины')),
                ('model', models.TextField(blank=True, null=True, verbose_name='Модель')),
                ('dealership', models.TextField(blank=True, null=True, verbose_name='Диллерский центр')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время получения')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ugc.category', verbose_name='Статус')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ugc.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': ('Заявку',),
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
