import telebot
import config
import au

bot = telebot.TeleBot(config.TOKEN)
#ID users
joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()
#Log users(ID,FIRST_NAME,LAST_NAME,USERNAME)
logFile = open("log.txt", "r")
logUsers = set()
for data in logFile:
    logUsers.add(data.strip())
logFile.close()



# Greeting
@bot.message_handler(commands=['start'])
def welcome(message):
    au = open('info/start.ogg', 'rb')
    bot.send_audio(message.chat.id, au,"{0.first_name}, если ты услышал(а) это приветствие, значит начиная со следующего, ты будешь ежедневно получать обещанные послания в формате голосовых сообщений 🎧\n\n<b>Как только я запишу что-то новое, я обязательно тебе отправлю</b> 😊".format(message.from_user, bot.get_me()), parse_mode='html')
    print("Пользователь запустил бота:\n" + str(message.from_user.id), str(message.from_user.first_name), str(message.from_user.username))

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)

    if not str(message.from_user.id) and str(message.from_user.first_name) in logUsers:
        logFile = open("log.txt", "a")
        logFile.write(str(message.from_user.id, message.from_user.first_name) + '\n')
        logUsers.add(message.form_user.id, message.from_user.first_name)

# New post for users
@bot.message_handler(commands=['sendnewpost'])
def newpost(message):
    for user in joinedUsers:
        au = open('info/1.ogg', 'rb')
        # bot.send_message(user, message).text[message.text.find(' '):]
        bot.send_audio(user, au,
                       "Это сегодня ☝️😍\n\n<a href='http://t.me/yupgrade_bot'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺".format(
                           message.from_user, bot.get_me()), parse_mode='html')
        print("Сообщение успешно отправлено")


@bot.message_handler(commands=['sendnewpost2'])
def newpost2(message):
    for i in joinedUsers:
        au = open('info/2.ogg', 'rb')
        bot.send_audio(i, au, "Удачи :)")
        print("Сообщение успешно отправлено_2")


@bot.message_handler(commands=['testbot'])
def testbot(message):
    bot.send_message(message.chat.id, "Бот работает :)\n")
    print("Бот работает :D")


# Log
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Бот, который ежедневно отправляет подбадривающие и мотивирующие голосовые сообщения от реального человека :)\n\n🎙| Бота озвучивает – Ronny*****\n👤| Сотрудничество – <a href='http://t.me/site_com_uz_officeal'>@site_com_uz_official</a>\nДата создания бота: 16.06.2022".format(message.from_user, bot.get_me()), parse_mode='html')

    """
x = ["{first_name}", "{last_name}"]
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
"""


# Run bot
# bot.polling(none_stop=True)
if __name__ == '__main__':
    bot.polling(none_stop=True)
