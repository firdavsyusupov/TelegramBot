from datetime import datetime
import telebot
import config
import random

bot = telebot.TeleBot(config.TOKEN)
# ID users
joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()


# Log users(ID,FIRST_NAME,LAST_NAME,USERNAME)
# logFile = open("log.txt", "r")
# logUsers = set()
# for data in logFile:
#     logUsers.add(data.strip())
# logFile.close()


# GREETING
@bot.message_handler(commands=['start'])
def welcome(message):
    au = open('info/start.ogg', 'rb')
    bot.send_audio(message.chat.id, au,
                   "{0.first_name}, если ты услышал(а) это приветствие, значит начиная со следующего, ты будешь ежедневно получать обещанные послания в формате голосовых сообщений 🎧\n\n<b>Как только я запишу что-то новое, я обязательно тебе отправлю</b> 😊".format(
                       message.from_user, bot.get_me()), parse_mode='html')
    print("Пользователь запустил бота:", message.from_user.id, message.from_user.first_name,
          message.from_user.last_name, message.from_user.username)

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

    logFile = open("log.txt", "a")
    logFile.write(f"{time} | Пользователь запустил бота: {id} {name} {lastname} {username} \n ")
    logFile.close()

    usersData = open("users.txt", "a")
    usersData.write(f"{time} | ID: {id} | Name: {name} | Last name: {lastname} | Username: @{username} \n")
    usersData.close()


# INFO
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Бот, который ежедневно отправляет подбадривающие и мотивирующие голосовые "
                                      "сообщения от реального человека :)\n\n🎙| Бота озвучивает – Ronny*****\n👤| "
                                      "Сотрудничество – <a "
                                      "href='http://t.me/firdavs_yusupov'>@firdavs_yusupov</a>\nДата "
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



# New post for users_____________________________________________________________________
# SEND VOICE №15
@bot.message_handler(commands=['sendnewpost'])
def newpost(message):
    for i in joinedUsers:
        au = open('info/16.ogg', 'rb')
        #list_file = open['info/1.ogg', 'info/2.ogg','info/3.ogg','info/4.ogg','info/5.ogg']
        #ran = random.choice(list_file)
        try:
            bot.send_audio(i, au,
                           "Хорошо?\n\n<a href=\'http://t.me/yupgrade_bot\'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺".format(
                               message.from_user, bot.get_me()), parse_mode='html')
            print("Сообщение успешно отправлено", message.chat.id, message.chat.first_name, message.chat.last_name, message.chat.username)
        except:
            pass
    id = message.from_user.id
    name = message.from_user.first_name
    lastname = message.from_user.last_name
    username = message.from_user.username
    time = datetime.now()

    logFile = open("log.txt", "a")
    logFile.write(f"{time} | Пользователь отправил сообщение №13: @{id} {name} {lastname} {username} \n ")
    logFile.close()


# ________________________________________________________________________________________

# CHECK BOT ↓ TEST BOT ↓ TEST CMD ↓ TEST ZONE ↓ TEST CODE ↓ CHECK BOT ↓ TEST BOT ↓ TEST CMD ↓ TEST ZONE ↓ TEST CODE
@bot.message_handler(commands=['testbot'])
def testbot(message):
    bot.send_message(message.chat.id, "Бот работает :)\n")
    print("Бот работает :D")


@bot.message_handler(commands=['asendinfopost'])
def infopost(message):
    for i in joinedUsers:
        bot.send_message(i, "Прошу всем".format(message.from_user), parse_mode='html')
        print("Сообщение успешно отправлено_", message.from_user.id, message.from_user.first_name,
              message.from_user.last_name, message.from_user.username)

@bot.message_handler(commands = ['asendmessage'])
def yousendmessage(message):
    for i in joinedUsers:
        try:#STOP STOP STOP STOP НАДО ДОРАБОТАТЬ ТЕКСТ!!!!!!!!!!!!!!!
            bot.send_message(i, "Друзья скоро выйдет новое обновление!\n\n<a href=\'http://t.me/yupgrade_bot\'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺".format(message.from_user, bot.get_me()), parse_mode='html')
            print("Сообщение успешно отправлено_", message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
        except:
            pass

# CHECK BOT ↑ TEST BOT ↑ TEST CMD ↑ TEST ZONE ↑ TEST CODE ↑ CHECK BOT ↑ TEST BOT ↑ TEST CMD ↑ TEST ZONE ↑ TEST CODE

# Run bot
# bot.polling(none_stop=True)
if __name__ == '__main__':
    bot.polling(none_stop=True)
