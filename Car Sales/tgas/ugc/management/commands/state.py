from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler, MessageHandler, Filters, CommandHandler
from .markup import *
from ugc.models import Profile, Message
from list.models import List, CarList, StocksCompany

# lIST DEALER CENTER
LIST_DEALER_CENTER = {
    'choose_region': 1,
    'choose_dealer_company': 2,
    'finish': 3
    }


def start_list_dealercenter(update, context):
    update.message.reply_text('Пожалуйста, выберите регион, где Вам удобнее приобрести автомобиль',
                              reply_markup=region)
    return LIST_DEALER_CENTER['choose_region']


def dealercenter_dealer_company(update, context):
    context.user_data['dealercenter_region'] = update.message.text
    update.message.reply_text("Выберите дилерское предприятие", reply_markup=dealer_company)
    return LIST_DEALER_CENTER['choose_dealer_company']


def finish_dealercenter(update, context):
    context.user_data['dealercenter_dealer_company'] = update.message.text
    post2 = List.objects.filter(region=context.user_data['dealercenter_region'])
    number = 0

    for info_post in post2:
        number += 1
        update.message.reply_text(f"Компания #{number}\n{info_post}", reply_markup=menu)

    if info_post == context.user_data['dealercenter_dealer_company']:
        update.message.reply_text(f"{info_post}")
    return ConversationHandler.END


# LIST OF THE COMPANY PRODUCT
LIST_COMPANY_PRODUCT = {
    'choose_type': 1,
    'choose_car': 2,
    'finish': 3
    }


def start_companyproduct(update, context):
    update.message.reply_text('Список продукции компании', reply_markup=cars)
    return LIST_COMPANY_PRODUCT['choose_type']


def companyproduct_car(update, context):
    context.user_data['product_company'] = update.message.text
    update.message.reply_text('Выберите модель которая вас интересует', reply_markup=car_models)
    return LIST_COMPANY_PRODUCT['choose_car']


def finish_companyproduct(update, context):
    post_companyproduct = CarList.objects.filter(type_car2=context.user_data['product_company'])
    numbers = 0

    for post_car in post_companyproduct:
        numbers += 1
        update.message.reply_text(f"Машина #{numbers}\n{post_car}", reply_markup=menu)

    if post_car == context.user_data['product_company']:
        update.message.reply_text(f"{post_car}")

    return ConversationHandler.END


# CARS IN STOCK
CAR_STOCK = {
    'choos_type': 1,
    'choos_car': 2,
    'fini': 3
    }


def start_carstock(update, context):
    update.message.reply_text('Автомобили в наличии ', reply_markup=cars)
    return CAR_STOCK['choos_type']


def carstock_car(update, context):
    context.user_data['car_stock'] = update.message.text
    update.message.reply_text('Выберите модель которая вас интересует', reply_markup=car_models)
    return CAR_STOCK['choos_car']


def finish_carstock(update, context):
    post_companyproduct = CarList.objects.filter(type_car2=context.user_data['car_stock']).values('name', 'quantity')
    a = sorted([[x['name'], x['quantity']] for x in post_companyproduct])
    numbers = 0
    for post_cars in a:
        numbers += 1
        update.message.reply_text(f"Машина #{numbers}\n"
                                  f"Название машины: {post_cars[0]}\n"
                                  f"Количество машин: {post_cars[1]}", reply_markup=menu)
    return ConversationHandler.END


CONTACT = {
        'contact': 1,
        'finish': 2
        }


def start_contact(update, context):
    update.message.reply_text("<b>Контактные данные:</b> \nНомер телефона: +998712535555 \n"
                              "Адресс: 2, 8 Ekhtirom Str., Тошкент 100100, Узбекистан", reply_markup=menu)
    loc_latitude = 41.279391337159794
    loc_longitude = 69.23887091148353

    context.bot.send_location(
        chat_id=update.message.from_user.id,
        latitude=float(loc_latitude),
        longitude=float(loc_longitude)
    )
    return CONTACT['contact']


def finish_contact(update):
    update.message.reply_text('Попробуйте заново еще раз!', reply_markup=menu)
    return ConversationHandler.END
