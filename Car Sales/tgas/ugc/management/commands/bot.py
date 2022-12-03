from django.core.management.base import BaseCommand
from django.conf import settings
# TELEGRAM BOT
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater
from telegram.ext import CommandHandler, ConversationHandler
from telegram.utils.request import Request
from telegram import ParseMode
# FILES
from ugc.models import Profile, Message
from list.models import StocksCompany
from .markup import *
from .OnlineAPP import *
from .state import *
from .log import *


class Command(BaseCommand):
    help = 'Телеграм-бот\n\n python ./manage.py bot    Launch the bot'

    def handle(self, *args, **options):
        # 1-Correct connection
        request = Request(
                connect_timeout=0.5,
                read_timeout=1.0,
                )
        bot = Bot(
                request=request,
                token=settings.TOKEN,
                )
        print('\nBot running ...\n')

        # 2-Message Handler
        updater = Updater(
                bot=bot,
                use_context=True,
                )
        # START
        start_bot = CommandHandler('start', start)
        updater.dispatcher.add_handler(start_bot)
        # ONLINE APPLICATION
        online_application = MessageHandler(Filters.regex("Онлайн заявка📝"), application)
        updater.dispatcher.add_handler(online_application)
        # Current shares of the company
        new_post = MessageHandler(Filters.regex("Текущие акции компании📈"), news_post)
        updater.dispatcher.add_handler(new_post)
        # BACK TO THE MENU
        back_menu = MessageHandler(Filters.regex("Назад"), back)
        updater.dispatcher.add_handler(back_menu)

        # CODE FOR STATE
        test_drive = ConversationHandler(  # Application for a test drive
                entry_points=[MessageHandler(Filters.regex("Заявка на тест драйв"), start_app_testdrive)],
                states={
                    1: [MessageHandler(Filters.text, process_testdrive_choose_dealer_company)],
                    2: [MessageHandler(Filters.text, finish_testdrive_app_testdrive)],
                    },
                fallbacks=[CommandHandler('stop', start)]
                )
        updater.dispatcher.add_handler(test_drive)

        app_product = ConversationHandler(  # Application for products
                entry_points=[MessageHandler(Filters.regex("Заявка на продукцию"), start_app_product)],
                states={
                    1: [MessageHandler(Filters.text, process_product_choose_model)],
                    2: [MessageHandler(Filters.text, process_product_choose_region)],
                    3: [MessageHandler(Filters.text, process_product_choose_dealer_company)],
                    4: [MessageHandler(Filters.text, finish_app_product)],
                    },
                fallbacks=[CommandHandler('stop', start)]
                )
        updater.dispatcher.add_handler(app_product)

        app_spare = ConversationHandler(  # Application for spare parts
                entry_points=[MessageHandler(Filters.regex("Заявка на запасные части"), start_app_spare)],
                states={
                    1: [MessageHandler(Filters.text, process_spare_choose_region)],
                    2: [MessageHandler(Filters.text, process_spare_choose_dealer_company)],
                    3: [MessageHandler(Filters.text, finish_app_spare)]
                    },
                fallbacks=[CommandHandler('stop', start)]
                )
        updater.dispatcher.add_handler(app_spare)

        app_service = ConversationHandler(  # Service request
                entry_points=[MessageHandler(Filters.regex("Заявка на сервис"), start_app_service)],
                states={
                    1: [MessageHandler(Filters.text, process_service_choose_dealership)],
                    2: [MessageHandler(Filters.text, process_service_choose_dealer_company)],
                    3: [MessageHandler(Filters.text, finish_app_service)]
                    },
                fallbacks=[CommandHandler('stop', start)]
                )
        updater.dispatcher.add_handler(app_service)

        list_dealercenter = ConversationHandler(  # List of dealerships
                entry_points=[MessageHandler(Filters.regex('Список дилерских центров 📑'), start_list_dealercenter)],
                states={
                    1: [MessageHandler(Filters.text, dealercenter_dealer_company)],
                    2: [MessageHandler(Filters.text, finish_dealercenter)]
                    },
                fallbacks=[CommandHandler('stop', start)]
                )
        updater.dispatcher.add_handler(list_dealercenter)

        list_cars = ConversationHandler(  # List of the company's products
                entry_points=[MessageHandler(Filters.regex('Список продукции компании 🗂'), start_companyproduct)],
                states={
                    1: [MessageHandler(Filters.text, companyproduct_car)],
                    2: [MessageHandler(Filters.text, finish_companyproduct)]
                    },
                fallbacks=[CommandHandler('stop', start)]
                )
        updater.dispatcher.add_handler(list_cars)

        car_in_stock = ConversationHandler(  # Cars in stock
                entry_points=[MessageHandler(Filters.regex('Автомобили в наличии 🛞'), start_carstock)],
                states={
                    1: [MessageHandler(Filters.text, carstock_car)],
                    2: [MessageHandler(Filters.text, finish_carstock)]
                    },
                fallbacks=[CommandHandler('stop', start)]
                )
        updater.dispatcher.add_handler(car_in_stock)

        me_contact = ConversationHandler(  # Contacts
                entry_points=[MessageHandler(Filters.regex('Контакты🪪'), start_contact)],
                states={
                    1: [MessageHandler(Filters.text, finish_contact)],
                    },
                fallbacks=[CommandHandler('stop', start)]
                )
        updater.dispatcher.add_handler(me_contact)

        # 3-Start infinite processing of incoming messages
        updater.start_polling()
        updater.idle()
