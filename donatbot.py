from telebot import types
import telebot
import config

bot = telebot.TeleBot(config.TOKEND)


@bot.message_handler(commands=['start'])
def start(message):
    photo_start = open('info/foto/start.jpg', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
# Buttons
    start_b = types.KeyboardButton('🤖 Bot')
    start_b1 = types.KeyboardButton('🗃 Projects')
    start_b2 = types.KeyboardButton('👨‍💻 Programmer')
    start_b3 = types.KeyboardButton('🔝 Other')
    markup.add(start_b, start_b1, start_b2, start_b3)
    bot.send_photo(message.chat.id, photo_start, "Привет, {0.first_name}!\n\n<b>Upgrade Донат</b> - это бот, в котором Вы сможете поддержать наш проект финансово 💸\n\nВсе ваши донаты пойдут на новое оборудование и на расширение наших проектов 🔥\n\nКуда хотите сделать перевод? 🔍".format(message.from_user), parse_mode='html', reply_markup = markup)

@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.chat.type == 'private':
        if message.text == 'Bot':
            bot.send_message(message.chat.id, 'В разработке...')
        elif message.text == "🗃 Projects":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            upgrade_b = types.KeyboardButton('📈 Upgrade')
            back = types.KeyboardButton('🔙 Back')
            markup.add(upgrade_b, back)

            bot.send_message(message.chat.id, '🗃 Projects', reply_markup = markup)
        elif message.text == "👨‍💻 Programmer":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            firdavs_b = types.KeyboardButton('👨‍💻 Firdavs')
            back = types.KeyboardButton('🔙 Back')
            markup.add(firdavs_b, back)

            bot.send_message(message.chat.id, '👨‍💻 Programmer', reply_markup = markup)
        elif message.text == "🔝 Other":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Back')
            markup.add(back)

            bot.send_message(message.chat.id, '🔝 Other', reply_markup = markup)
        elif message.text == "🔙 Back":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            start_b = types.KeyboardButton('🤖 Bot')
            start_b1 = types.KeyboardButton('🗃 Projects')
            start_b2 = types.KeyboardButton('👨‍💻 Programmer')
            start_b3 = types.KeyboardButton('🔝 Other')
            markup.add(start_b, start_b1, start_b2, start_b3)

            bot.send_message(message.chat.id, '🔙 Back', reply_markup = markup)

# RUN
if __name__ == '__main__':
    bot.polling(none_stop=True)