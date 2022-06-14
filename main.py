import telebot
import config

bot = telebot.TeleBot(config.TOKEN)
# Greeting
@bot.message_handler(commands=['start'])
def welcome(message):
    au = open('info/start.ogg', 'rb')
    bot.send_audio(message.chat.id, au, "{0.first_name}, если ты услышал(а) это приветствие, значит начиная со следующего, ты будешь ежедневно получать обещанные послания в формате голосовых сообщений 🎧\n\n<b>Как только я запишу что-то новое, я обязательно тебе отправлю</b> 😊".format(message.from_user, bot.get_me()), parse_mode='html')

# Info
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id)

'''
@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.it, message.text)
'''


# Run bot
bot.polling(none_stop=True)
