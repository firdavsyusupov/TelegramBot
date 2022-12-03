from django.db import models
from django.urls import reverse


class Profile(models.Model):  # List of users
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя в соц сети',
        unique=True,
        )
    name = models.TextField(
        verbose_name='Имя пользователя',
        )

    def __str__(self):
        return f'#{self.external_id}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Message(models.Model):  # List of requests from users
    profile = models.ForeignKey(to='ugc.Profile', verbose_name='Профиль', on_delete=models.PROTECT)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Статус")
    text = models.TextField(verbose_name='Заявка', blank=True, null=True)
    region = models.TextField(verbose_name='Регион', blank=True, null=True)
    dealer_company = models.TextField(verbose_name='Дилерское предприятие', blank=True, null=True)
    type_car = models.TextField(verbose_name='Тип машины', blank=True, null=True)
    model = models.TextField(verbose_name='Модель', blank=True, null=True)
    dealership = models.TextField(verbose_name='Диллерский центр', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Время получения', auto_now_add=True)

    def __str__(self):
        return f'Номер сообщении {self.pk} от {self.profile}'

    class Meta:
        verbose_name = 'Заявку',
        verbose_name_plural = 'Заявки'


class Category(models.Model):  # Categories for the status in the application
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
