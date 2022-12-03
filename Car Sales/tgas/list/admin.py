from django.contrib import admin

# Register your models here.
from .models import List, CarList, StocksCompany, CategoryCars
from .form import ListForm, CarListForm


@admin.register(List)  # List of dealer companies
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'region', 'dealer_company', 'name')
    form = ListForm


@admin.register(CarList)  # List of the company's products
class CarListAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_car2', 'quantity', 'car_info')
    form = CarListForm


@admin.register(CategoryCars)  # Car categories
class CategoryCarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(StocksCompany)  # Shares from the company
class StocksCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'date')
    