from datetime import datetime
import telebot
import config


bot = telebot.TeleBot(config.TOKEN)
# ID users
joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()
# Log users(ID,FIRST_NAME,LAST_NAME,USERNAME)
#logFile = open("log.txt", "r")
# logUsers = set()
# for data in logFile:
#     logUsers.add(data.strip())
#logFile.close()
# def variables():
#     id = message.from_user.id
#     name = message.from_user.first_name
#     lastname = message.from_user.last_name
#     username = message.from_user.username
#     time = datetime.now()

# GREETING
@bot.message_handler(commands=['start'])
def welcome(message):
    au = open('info/start.ogg', 'rb')
    bot.send_audio(message.chat.id, au,
                   "{0.first_name}, если ты услышал(а) это приветствие, значит начиная со следующего, ты будешь ежедневно получать обещанные послания в формате голосовых сообщений 🎧\n\n<b>Как только я запишу что-то новое, я обязательно тебе отправлю</b> 😊".format(
                       message.from_user, bot.get_me()), parse_mode='html')
    print("Пользователь запустил бота:" , message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id
                              ) + '\n')
        joinedUsers.add(message.chat.id)
    id = message.from_user.id
    name = message.from_user.first_name
    lastname = message.from_user.last_name
    username = message.from_user.username
    time = datetime.now()

   #if not str(message.from_user.id) and str(message.from_user.first_name) in logUsers:
    logFile = open("log.txt", "a")
    logFile.write(f"{time} | Пользователь запустил бота: {id} {name} {lastname} {username} \n ")
        #logUsers.add(message.form_user.id)
    logFile.close()

# INFO
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Бот, который ежедневно отправляет подбадривающие и мотивирующие голосовые "
                                      "сообщения от реального человека :)\n\n🎙| Бота озвучивает – Ronny*****\n👤| "
                                      "Сотрудничество – <a "
                                      "href='http://t.me/site_com_uz_officeal'>@site_com_uz_official</a>\nДата "
                                      "создания бота: 16.06.2022".format(message.from_user, bot.get_me()),
                     parse_mode='html')
    id = message.from_user.id
    name = message.from_user.first_name
    lastname = message.from_user.last_name
    username = message.from_user.username
    time = datetime.now()

    # if not str(message.from_user.id) and str(message.from_user.first_name) in logUsers:
    logFile = open("log.txt", "a")
    logFile.write(f"{time} | Пользователь просматривает информацию: {id} {name} {lastname} {username} \n ")
    # logUsers.add(message.form_user.id)
    logFile.close()

@bot.message_handler(commands=['ac'
                               'md'])
def admincmd(message):
    bot.send_message(message.chat.id, "Ежедневные аудио:\n\n/sendnewpost3\n\n/sendnewpost4\n\n/sendnewpost5\n\n/sendnewpost6\n\n/sendnewpost7\n\n/sendnewpost8\n\n/sendnewpost9\n\n/sendnewpost10\n\n/sendnewpost11\n\n/sendnewpost12\n\n/sendnewpost13\n\n/sendnewpost14\n\n/sendnewpost15\n\n/sendnewpost16\n\n/sendnewpost17\n\n/sendnewpost18\n\n/sendnewpost19")
    id = message.from_user.id
    name = message.from_user.first_name
    lastname = message.from_user.last_name
    username = message.from_user.username
    time = datetime.now()

    # if not str(message.from_user.id) and str(message.from_user.first_name) in logUsers:
    logFile = open("log.txt", "a")
    logFile.write(f"{time} | ВНИМАНИЕ!WARM!admincmd: {id} {name} {lastname} {username} \n ")
    # logUsers.add(message.form_user.id)
    logFile.close()

# New post for users_____________________________________________________________________
@bot.message_handler(commands=['sendnewpost1'])
def newpost(message):
    for user in joinedUsers:
        au = open('info/1.ogg', 'rb')
        # bot.send_message(user, message).text[message.text.find(' '):]
        bot.send_audio(user, au,
                       "Это сегодня ☝️😍\n\n<a href='http://t.me/yupgrade_bot'>© Твой Апгрейд ♥</a>\n\nПоделись с "
                       "друзьями 🥺".format(message.from_user, bot.get_me()), parse_mode='html')
        print("Сообщение успешно отправлено_1")

@bot.message_handler(commands=['sendnewpost2'])
def newpost2(message):
    for i in joinedUsers:
        au = open('info/2.ogg', 'rb')
        bot.send_audio(i, au, "Красивого тебе дня ☀️\n\n<a href='http://t.me/yupgrade_bot'>© Твой Апгрейд ♥</a> "
                              "\n\nПоделись с друзьями 🥺".format(message.from_user, bot.get_me()), parse_mode='html')
        print("Сообщение успешно отправлено_2")

@bot.message_handler(commands=['sendnewpost3'])
def newpost(message):
    for i in joinedUsers:
        au = open('info/3.ogg', 'rb')
        bot.send_audio(i, au,
                       "Не забывай про это ☝️\n\n<a href=\'http://t.me/yupgrade_bot\'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺".format(
                           message.from_user, bot.get_me()), parse_mode='html')
        print("Сообщение успешно отправлено_3", message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)

@bot.message_handler(commands =['sendnewpost4'])
def newpost(message):
    for i in joinedUsers:
        au = open('info/.ogg4', 'rb')
        bot.send_audio(i, au, "Пусть так и будет ☝️\n\n<a href=\'http://t.me/yupgrade_bot\'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺".format(message.from_user, bot.get_me()), parse_mode='html')
        print("Сообщение успешно отправлено_4", message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)

@bot.message_handler(commands = ['sendnewpost5'])
def newpost(message):
    for i in joinedUsers:
        au = open('info/5.ogg', 'rb')
        bot.send_audio(i, au, "Сделай это ☝️\n\n<a href=\'http://t.me/yupgrade_bot\'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺".format(message.from_user, bot.get_me()), parse_mode='html')
        print("Сообщение успешно отправлено_5", message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
# ________________________________________________________________________________________

# CHECK BOT ↓ TEST BOT ↓ TEST CMD ↓ TEST ZONE ↓ TEST CODE ↓ CHECK BOT ↓ TEST BOT ↓ TEST CMD ↓ TEST ZONE ↓ TEST CODE
@bot.message_handler(commands=['testbot'])
def testbot(message):
    bot.send_message(message.chat.id, "Бот работает :)\n")
    print("Бот работает :D")

@bot.message_handler(commands=['sendinfopost'])
def infopost(message):
    for i in joinedUsers:
        bot.send_message(i, "Любовь уже есть в твоей жизни, но ты не сможешь почувствовать её, пока ищешь её снаружи. Ничто и никто не даст тебе той любви, которую можно найти только внутри себя. Достижения, люди и события не сделают тебя счастливым, пока ты не осознаешь, что источник счастья и любви находится внутри тебя самого. <b>Всегда.</b>".format(message.from_user), parse_mode='html')
        print("Сообщение успешно отправлено_", message.from_user.id, message.from_user.first_name,message.from_user.last_name, message.from_user.username)



# CHECK BOT ↑ TEST BOT ↑ TEST CMD ↑ TEST ZONE ↑ TEST CODE ↑ CHECK BOT ↑ TEST BOT ↑ TEST CMD ↑ TEST ZONE ↑ TEST CODE

# Run bot
# bot.polling(none_stop=True)
if __name__ == '__main__':
    bot.polling(none_stop=True)
