from django.db import models
from django.urls import reverse


class List(models.Model):   # List of dealer companies
    region = models.TextField(verbose_name='Регион', default='Укажите регион!')
    dealer_company = models.TextField(verbose_name='Наименования компании')
    name = models.TextField(verbose_name='Полная информация о компании')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Список дилерских центров 📑'
        verbose_name_plural = 'Список дилерских центров 📑'
        ordering = ['id']


class CarList(models.Model):    # List of the company's products
    type_car = models.ForeignKey('CategoryCars', on_delete=models.PROTECT, null=True, verbose_name="Тип автомобиля")
    type_car2 = models.TextField(verbose_name='Тип автомобиля')
    quantity = models.TextField(verbose_name='Кол-во автомобилей')
    name = models.TextField(verbose_name='Модель автомобиля')
    car_info = models.TextField(verbose_name='Информация о автомобиле')

    def __str__(self):
        return self.car_info

    class Meta:
        verbose_name = 'Список продукции компании 🗂'
        verbose_name_plural = 'Список продукции компании 🗂'


class CategoryCars(models.Model):   # Car categories
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория автомобиля'
        verbose_name_plural = 'Категории автомобилей'
        ordering = ['id']


class StocksCompany(models.Model):  # Shares from the company
    date = models.DateTimeField(verbose_name='Время получения', auto_now_add=True)
    post = models.TextField(verbose_name='Новая акция')

    def get_absolute_url(self):
        return self.post

    class Meta:
        verbose_name = 'Акция от компании'
        verbose_name_plural = 'Акции от компании'
        ordering = ['id']
