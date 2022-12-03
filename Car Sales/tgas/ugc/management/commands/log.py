from telegram import Bot
from telegram import Update
from telegram.utils.request import Request
from telegram import ParseMode
from list.models import StocksCompany
from .markup import *


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)

        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e
    return inner


@log_errors  # Getting started with the telegram bot
def start(update, context):
    update.message.reply_text("Здравствуйте, на связи бот\n", reply_markup=menu)


@log_errors  # Leave an online application
def application(update, context):
    message = update.message.text
    update.message.reply_text("Выберите в какой раздел вы хотите оставить заявку", reply_markup=online_app)


@log_errors  # View the company's current shares
def news_post(update, context):
    news = StocksCompany.objects.values_list('post', flat=True)
    for posty in news:
        update.message.reply_text(f"\n{posty}", reply_markup=menu)


@log_errors  # Go back to the main menu
def back(update, context):
    message = update.message.text
    update.message.reply_text('Вы вернулись в главное меню', reply_markup=menu)


@log_errors  # Contact section
def contact(update, context):
    message = update.message.text
    update.message.reply_text("<b>Контактные данные:</b> \nНомер телефона: +998712535555 \n"
                              "Адресс: 2, 8 Ekhtirom Str., Тошкент 100100, Узбекистан")
