from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler, MessageHandler, Filters, CommandHandler
from .markup import *
from ugc.models import Profile, Message
from list.models import List, CarList, StocksCompany


# APPLICATION FOR A TEST DRIVE
STATE_APP_TESTDRIVE = {
        'choose_region': 1,
        'choose_dealer_company': 2,
        'finish': 3
        }


# APPLICATION FOR A TEST DRIVE
def start_app_testdrive(update, context):  # Select a region
    context.user_data['testdrive'] = update.message.text
    update.message.reply_text('Выберите пожалуйста регион', reply_markup=region)
    return STATE_APP_TESTDRIVE['choose_region']


def process_testdrive_choose_dealer_company(update, context):  # Choose a dealer company
    context.user_data['testdrive_region'] = update.message.text
    update.message.reply_text("Выберите дилерское предприятие", reply_markup=ReplyKeyboardRemove())

    list_dealer_company = List.objects.filter(region=context.user_data['testdrive_region'])
    number = 0

    for info_post in list_dealer_company:
        number += 1
        update.message.reply_text(f"Компания #{number}\n{info_post}")

    update.message.reply_text('Напишите название диллерской предприятии')
    return STATE_APP_TESTDRIVE['choose_dealer_company']


def finish_testdrive_app_testdrive(update, context):
    context.user_data['testdrive_dealer_company'] = update.message.text
    chat_id = update.message.chat_id
    text = update.message.text

    # CHECK PROFILE TRUE OR FALSE
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,

        )

    # SAVE MESSAGE FROM USER
    new_message = Message(
                profile=p,
                text=context.user_data['testdrive'],
                region=context.user_data['testdrive_region'],
                dealer_company=context.user_data['testdrive_dealer_company'],
                )
    new_message.save()

    reply_text = f'Номер заявки: #{new_message.pk}\n\n{text}'
    update.message.reply_text(text=reply_text,)
    update.message.reply_text("Ваша заявка принята на обработку, скоро с Вами свяжутся наши дилеры.",
                              reply_markup=ReplyKeyboardRemove())

    update.message.reply_text('Главное меню', reply_markup=menu)
    return ConversationHandler.END


# APPLICATION FOR PRODUCTS
STATE_APP_PRODUCT = {
        'choose_type_car': 1,
        'choose_model': 2,
        'choose_region': 3,
        'choose_dealer_company': 4,
        'finish': 5
        }


def start_app_product(update, context):  # Choose the type of car
    context.user_data['appproduct'] = update.message.text
    update.message.reply_text('Выберите тип автомобиля', reply_markup=cars)
    return STATE_APP_PRODUCT['choose_type_car']


def process_product_choose_model(update, context):  # Select a model
    context.user_data['appproduct_type_car'] = update.message.text
    update.message.reply_text("Выберите модель")

    list_models = CarList.objects.filter(type_car2=context.user_data['appproduct_type_car']).values('name')
    sortedByABC = sorted([x['name'] for x in list_models])
    numbers = 0
    update.message.reply_text('TESTY')

    for model in sortedByABC:
        numbers += 1
        update.message.reply_text(f"Машина #{numbers}\n"
                                  f"Модель машины: {model}\n", reply_markup=ReplyKeyboardRemove())

    return STATE_APP_PRODUCT['choose_model']


def process_product_choose_region(update, context):  # Select a region
    context.user_data['appproduct_model'] = update.message.text
    update.message.reply_text("Выберите пожалуйста регион", reply_markup=region)
    return STATE_APP_PRODUCT['choose_region']


def process_product_choose_dealer_company(update, context):  # Choose a dealer company
    context.user_data['appproduct_region'] = update.message.text
    update.message.reply_text('Выберите дилерское предприятие', reply_markup=ReplyKeyboardRemove())
    dealers_company = List.objects.filter(region=context.user_data['appproduct_region'])
    number = 0

    for info_post in dealers_company:
        number += 1
        update.message.reply_text(f"Компания #{number}\n{info_post}")

    update.message.reply_text('Напишите название диллерской предприятии', reply_markup=ReplyKeyboardRemove())
    return STATE_APP_PRODUCT['choose_dealer_company']


def finish_app_product(update, context):
    context.user_data['appproduct_dealer_company'] = update.message.text
    chat_id = update.message.chat_id
    text = update.message.text

    # CHECK PROFILE TRUE OR FALSE
    p, _ = Profile.objects.get_or_create(
                                external_id=chat_id,
                                )

    # SAVE MESSAGE FROM USER
    new_message = Message(
            profile=p,
            text=context.user_data['appproduct'],
            type_car=context.user_data['appproduct_type_car'],
            model=context.user_data['appproduct_model'],
            region=context.user_data['appproduct_region'],
            dealer_company=context.user_data['appproduct_dealer_company']
            )
    new_message.save()

    reply_text = f'Номер заявки: #{new_message.pk}\n\n{text}'
    update.message.reply_text(text=reply_text,)
    update.message.reply_text("Ваша заявка принята на обработку, скоро с Вами свяжутся наши дилеры",
                              reply_markup=ReplyKeyboardRemove())

    update.message.reply_text('Главное меню', reply_markup=menu)
    return ConversationHandler.END


# REQUEST FOR SPARE PARTS
STATE_APP_SAPRE = {
        'choose_dealership': 1,
        'choose_region': 2,
        'choose_dealer_company': 3,
        'finish': 4
        }


# REQUEST FOR SPARE PARTS
def start_app_spare(update, context):
    context.user_data['appspare'] = update.message.text
    update.message.reply_text('Список дилерских центров', reply_markup=IN_DEVELOPMENT)
    return STATE_APP_SAPRE['choose_dealership']


def process_spare_choose_region(update, context):
    context.user_data['appspare_dealership'] = update.message.text
    update.message.reply_text("Выберите пожалуйста регион", reply_markup=region)
    return STATE_APP_SAPRE['choose_region']


def process_spare_choose_dealer_company(update, context):
    context.user_data['appspare_region'] = update.message.text
    update.message.reply_text("Выберите дилерское предприятие", reply_markup=ReplyKeyboardRemove())
    dealers_company = List.objects.filter(region=context.user_data['appspare_region'])
    number = 0

    for info_post in dealers_company:
        number += 1
        update.message.reply_text(f"Компания #{number}\n{info_post}")

    update.message.reply_text('Напишите название диллерской предприятии')
    return STATE_APP_SAPRE['choose_dealer_company']


def finish_app_spare(update, context):
    context.user_data['appspare_dealer_company'] = update.message.text
    chat_id = update.message.chat_id
    text = update.message.text

    # CHECK PROFILE TRUE OR FALSE
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
    )
    # SAVE MESSAGE FROM USER
    new_message = Message(
            profile=p,
            text=context.user_data['appspare'],
            dealership=context.user_data['appspare_dealership'],
            region=context.user_data['appspare_region'],
            dealer_company=context.user_data['appspare_dealer_company']
            )
    new_message.save()

    reply_text = f'Номер заявки: #{new_message.pk}\n\n{text}'
    update.message.reply_text(text=reply_text,)
    update.message.reply_text("Ваша заявка принята на обработку, скоро с Вами свяжутся наши дилеры.",
                              reply_markup=ReplyKeyboardRemove())

    update.message.reply_text('Главное меню', reply_markup=menu)
    return ConversationHandler.END


# SERVICE REQUEST
STATE_APP_SERVICE = {
        'choose_dealership': 1,
        'choose_region': 2,
        'choose_dealer_company': 3,
        'finish': 4
        }


# SERVICE REQUEST
def start_app_service(update, context):
    context.user_data['appservice'] = update.message.text
    update.message.reply_text('Список дилерских центров', reply_markup=IN_DEVELOPMENT)
    return STATE_APP_SERVICE['choose_dealership']


def process_service_choose_dealership(update, context):
    context.user_data['appservice_dealership'] = update.message.text
    update.message.reply_text("Выберите пожалуйста регион", reply_markup=region)
    return STATE_APP_SERVICE['choose_region']


def process_service_choose_dealer_company(update, context):
    context.user_data['appservice_region'] = update.message.text
    update.message.reply_text("Выберите дилерское предприятие", reply_markup=ReplyKeyboardRemove())
    dealers_company = List.objects.filter(region=context.user_data['appservice_region'])
    number = 0

    for info_post in dealers_company:
        number += 1
        update.message.reply_text(f"Компания #{number}\n{info_post}")
    return STATE_APP_SERVICE['choose_dealer_company']


def finish_app_service(update, context):
    context.user_data['appservice_dealer_company'] = update.message.text
    chat_id = update.message.chat_id
    text = update.message.text
    # CHECK PROFILE TRUE OR FALSE

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
    )
    # SAVE MESSAGE FROM USER
    new_message = Message(
            profile=p,
            text=context.user_data['appservice'],
            dealership=context.user_data['appservice_dealership'],
            region=context.user_data['appservice_region'],
            dealer_company=context.user_data['appservice_dealer_company']
            )
    new_message.save()

    reply_text = f'Номер заявки: #{new_message.pk}\n\n{text}'
    update.message.reply_text(text=reply_text,)
    update.message.reply_text("Ваша заявка принята на обработку, скоро с Вами свяжутся наши дилеры.",
                              reply_markup=ReplyKeyboardRemove())

    update.message.reply_text('Главное меню', reply_markup=menu)
    return ConversationHandler.END
