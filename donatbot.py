from telebot import types
import telebot
import config

bot = telebot.TeleBot(config.TOKEND)
# ID users
joinedFile = open("iddonatbot.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

@bot.message_handler(commands=['start'])
def start(message):
    photo_start = open('info/foto/start.jpg', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
# Buttons
    start_b = types.KeyboardButton('💳 Uzcard')
    start_b1 = types.KeyboardButton('📲 Click')
    start_b2 = types.KeyboardButton('👨‍💻 Programmers')
    start_b3 = types.KeyboardButton('🔝 Other')
    markup.add(start_b, start_b1, start_b2, start_b3)
    bot.send_photo(message.chat.id, photo_start, "Привет, {0.first_name}!\n\n<b>Upgrade Донат</b> - это бот, в котором Вы сможете поддержать наш проект финансово 💸\n\nВсе ваши донаты пойдут на новое оборудование и на расширение наших проектов 🔥\n\nКуда хотите сделать перевод? 🔍".format(message.from_user), parse_mode='html', reply_markup = markup)
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)

@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.chat.type == 'private':
        if message.text == '💳 Uzcard':
            bot.send_message(message.chat.id, '💳 Наш Uzcard:\n\n<code>8600330449389160</code> - карта\n\nСпасибо большое за донат 🫂\n\nПосле отправки, напишите мне в ЛС— @firdavs_yusupov'.format(message.from_user), parse_mode='html')
        elif message.text == "📲 Click":
            qr_click = open('info/foto/click.jpg', 'rb')
            bot.send_photo(message.chat.id, qr_click, "Чтобы удобно перевести деньги через CLICK нам на карту, Вы можете:\n- отсканировать QR-код приложением CLICK Evolution\n- отправить это сообщение в Telegram-бот @clickuz\n- пройти по ссылке ниже\n\nПолучатель: YUSUPOV FIRDAVS\nМоя карта: IPTK***9160 (UZCARD)\n\nhttps://my.click.uz/clickp2p/3FF1A5157E7FBCF80F8540365C8E3792972D6C73F1B028793D8EDA8D41450611")

            #bot.send_message(message.chat.id, '🗃 Projects', reply_markup = markup)


# RUN
if __name__ == '__main__':
    bot.polling(none_stop=True)