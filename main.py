import telebot
import config
import au

bot = telebot.TeleBot(config.TOKEN)
joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()


# Greeting
@bot.message_handler(commands=['start'])
def welcome(message):
    au = open('info/start.ogg', 'rb')
    bot.send_audio(message.chat.id, au, "{0.first_name}, если ты услышал(а) это приветствие, значит начиная со следующего, ты будешь ежедневно получать обещанные послания в формате голосовых сообщений 🎧\n\n<b>Как только я запишу что-то новое, я обязательно тебе отправлю</b> 😊".format(message.from_user, bot.get_me()), parse_mode='html')
    print("Пользователь запустил бота:\n" + "Name: " + "\nSurname: " + "\nUsername: ")
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)

# New post for users
@bot.message_handler(commands=['sendnewpost'])
def newpost(message):
    for user in joinedUsers:
        au = open('info/1.ogg', 'rb')
        #bot.send_message(user, message).text[message.text.find(' '):]
        bot.send_audio(user, au, "Это сегодня ☝️😍\n\n<a href='http://t.me/yupgrade_bot'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺".format(message.from_user, bot.get_me()), parse_mode='html')
        print("Сообщение успешно отправлено!")

# Info
'''
log = ["{first_name}", "{last_name}"]
    file = open("log.txt", 'w+')
    for i in log:
        file.write(i + '\n')
    file.close()
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id)


@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.it, message.text)
'''


# Run bot
bot.polling(none_stop=True)
