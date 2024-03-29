from datetime import datetime
from telebot import types
import telebot
import config

bot = telebot.TeleBot(config.TOKEND)
# ID users
joinedFile = open("log/dup/joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()


@bot.message_handler(commands=['start'])
def start(message):
    photo_start = open('info/image/start.jpg', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Buttons
    start_b = types.KeyboardButton('💳 Uzcard')
    start_b1 = types.KeyboardButton('📲 Click')
    start_b3 = types.KeyboardButton('🔝 Other')
    start_b4 = types.KeyboardButton('📇 Топ донатеров')
    markup.add(start_b, start_b1, start_b3, start_b4)
    bot.send_photo(message.chat.id, photo_start,
                   "Привет, {0.first_name}!\n\n<b>Upgrade Донат</b> - это бот, в котором Вы сможете поддержать наш проект финансово 💸\n\nВсе ваши донаты пойдут на новое оборудование и на расширение наших проектов 🔥\n\nКуда хотите сделать перевод? 🔍".format(
                       message.from_user), parse_mode='html', reply_markup=markup)
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("log/dup/joined.txt", "a")
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)
    id = message.from_user.id
    name = message.from_user.first_name
    lastname = message.from_user.last_name
    username = message.from_user.username
    time = datetime.now()
    logFile = open("log/dup/log.txt", "a")
    logFile.write(f"{time} | NEW user: @{id} {name} {lastname} {username} \n ")
    logFile.close()


@bot.message_handler(commands=['updatebot'])
def botupdate(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Buttons
    start_b = types.KeyboardButton('ОБНОВИТЬ')
    markup.add(start_b)
    for i in joinedUsers:
        try:
            bot.send_message(i, "Ваш бот устарел. Пожалуйста, обновите бота".format(message.from_user, bot.get_me()), reply_markup=markup)

        except:
            pass

@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.chat.type == 'private':
        if message.text == '💳 Uzcard':
            bot.send_message(message.chat.id,
                             '💳 Наш Uzcard:\n\n<code>6262720002327453</code> - карта\n\nСпасибо большое за донат 🫂\n\nПосле отправки, напишите мне в ЛС— @firdavs_yusupov'.format(
                                 message.from_user), parse_mode='html')

        elif message.text == "📲 Click":
            qr_click = open('info/image/click.jpg', 'rb')
            bot.send_photo(message.chat.id, qr_click,
                           "Чтобы удобно перевести деньги через CLICK нам на карту, Вы можете:\n- отсканировать QR-код приложением CLICK Evolution\n- отправить это сообщение в Telegram-бот @clickuz\n- пройти по ссылке ниже\n\nПолучатель: YUSUPOV FIRDAVS\nМоя карта: AAB***7453 (UZCARD)\n\nhttps://my.click.uz/clickp2p/F907B946693836900BD2EA6E807F9AA68BE12EBB46F1866D0EB96661599623DD")

        # elif message.text == '👨‍💻 Programmers':
        #    bot.send_message(message.cha.id, 'В разработке...'.format(message.from_user), parse_mode='html')

        elif message.text == '🔝 Other':
            bot.send_message(message.chat.id,
                             '<b>Упс...</b> 😬\n\nЕсли Вы не нашли подходящий способ для перевода, напишите мне в ЛС — <a href="https://t.me/firdavs_yusupov">@firdavs_yusupov</a>'.format(
                                 message.from_user), parse_mode='html')

        elif message.text == '📇 Топ донатеров':
            top_donate = open('info/image/top.jpg', 'rb')  # https://streamdps.ru/panels/55757/
            bot.send_photo(message.chat.id, top_donate, "<b>📇 ТОП-3 донатеров:</b>\n\n"
                                                        "▪️1. JaRuLe — 20000 SUM\n"
                                                        "▪️2. Скоро\n"
                                                        "▪️3. Скоро\n"
            # "▪️4. Скоро\n"
            # "▪️5. К\n"
                                                        "\n❤️Огромное спасибо и всем остальным за поддержку\n\n"
                                                        "Если Вы сделали донат больше топ-3, но не видите себя в списке, сообщите мне — @firdavs_yusupov 💬".format(
                message.from_user), parse_mode='html')

        elif message.text == 'ОБНОВИТЬ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            # Buttons
            start_b = types.KeyboardButton('💳 Uzcard')
            start_b1 = types.KeyboardButton('📲 Click')
            # start_b2 = types.KeyboardButton('👨‍💻 Programmers')
            start_b3 = types.KeyboardButton('🔝 Other')
            start_b4 = types.KeyboardButton('📇 Топ донатеров')
            markup.add(start_b, start_b1, start_b3, start_b4)
            bot.send_message(message.from_user.id, 'Бот успешно обновлен :)', reply_markup=markup)



# RUN
while True:
    try:
        if __name__ == '__main__':
            bot.polling(none_stop=True)

    except:
        continue
    break
