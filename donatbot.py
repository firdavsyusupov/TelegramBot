from telebot import types
import telebot
import config

bot = telebot.TeleBot(config.TOKEND)


@bot.message_handler(commands=['start'])
def start(message):
    photo_start = open('info/foto/start.jpg', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
# Buttons
    item1 = types.KeyboardButton('Bot')
    item2 = types.KeyboardButton('Projects')
    item3 = types.KeyboardButton('Programmer')
    markup.add(item1, item2, item3)
    bot.send_photo(message.chat.id, photo_start, "Привет, {0.first_name}!\n\n<b>Upgrade Донат</b> - это бот, в котором Вы сможете поддержать наш проект финансово 💸\n\nВсе ваши донаты пойдут на новое оборудование и на расширение наших проектов 🔥\n\nКуда хотите сделать перевод? 🔍".format(message.from_user), parse_mode='html', reply_markup = markup)


# RUN
if __name__ == '__main__':
    bot.polling(none_stop=True)