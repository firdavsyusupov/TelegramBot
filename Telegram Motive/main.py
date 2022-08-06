from datetime import datetime
import telebot
import config
import random

bot = telebot.TeleBot(config.TOKEN)
# ID users
joinedFile = open("log/up/joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

podcastFile = open('log/podcast/id.txt', 'r')
podcastUsers = set()
for i in podcastFile:
    podcastUsers.add(i.strip())
podcastFile.close()

# @bot.message_handler(commands=['testfunclallalblablabla'])
# def variables(message):
#     global id
#     id = int(message.from_user.id)
#     global first_name
#     first_name = message.from_user.first_name
#     global last_name
#     last_name = message.from_user.last_name
#     global username
#     username = message.from_user.username
#     global time
#     time = datetime.now()



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
        joinedFile = open("log/up/joined.txt", "a")
        joinedFile.write(str(message.chat.id
                             ) + '\n')
        joinedUsers.add(message.chat.id)
    id = message.from_user.id
    name = message.from_user.first_name
    lastname = message.from_user.last_name
    username = message.from_user.username
    time = datetime.now()

    logFile = open("log/up/log.txt", "a")
    logFile.write(f"{time} | Пользователь запустил бота: {id} {name} {lastname} {username} \n ")
    logFile.close()

    usersData = open("log/up/users.txt", "a")
    usersData.write(f"{time} | ID: {id} | Name: {name} | Last name: {lastname} | Username: @{username} \n")
    usersData.close()


# INFO
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Бот, который ежедневно отправляет подбадривающие и мотивирующие голосовые "
                                      "сообщения от реального человека :)\n\n🎙| Бота озвучивает – Ronny*****\n👤| "
                                      "Сотрудничество – <a "
                                      "href='http://t.me/firdavs_yusupov'>@firdavs_yusupov</a>\nДата "
                                      "создания бота: 16.06.2022".format(message.from_user, bot.get_me()), parse_mode='html')
    id = message.from_user.id
    name = message.from_user.first_name
    lastname = message.from_user.last_name
    username = message.from_user.username
    time = datetime.now()
    # if not str(message.from_user.id) and str(message.from_user.first_name) in logUsers:
    logFile = open("log/up/log.txt", "a")
    logFile.write(f"{time} | Пользователь просматривает информацию: {id} {name} {lastname} {username} \n ")
    # logUsers.add(message.form_user.id)
    logFile.close()

@bot.message_handler(commands=['donat'])
def send_donat(message):
    bot.send_message(message.chat.id, "Ежедневно мы трудимся над созданием и улучшением наших проектов, которые вдохновляют и мотивируют многих из Вас. Все голосовые которые Вы слышали или только услышите - это записываем мы лично, а не какой-либо бот."
                                      "\n\nБот «Твой Апгрейд» - это лишь удобная площадка, через которую можно делать рассылку всем Вам. Чтобы содержать данного бота, мы ежемесячно его оплачиваем."
                                      "\n\nЕсли Вы хотите поддержать наш труд финансово, можете выбрать любую удобную платежную систему и сделать перевод - @yudonat_bot"
                                      "\n\n<b>Все ваши донаты пойдут на новое оборудование и на расширение наших проектов.</b>".format(message.from_user, bot.get_me()), parse_mode='html')



# New post for users_____________________________________________________________________
# SEND VOICE №25
@bot.message_handler(commands=['sendnewpost'])
def newpost(message):
    print('Ваше сообщение отправляется...')
    voice = open('info/voice.txt', 'r')
    id_voice = voice.readlines()[-1]
    voice.close()
    num = 0
    for i in joinedUsers:
        au = open(f'info/{id_voice}.ogg', 'rb' )
        #list_file = open['info/1.ogg', 'info/2.ogg','info/3.ogg','info/4.ogg','info/5.ogg']
        #ran = random.choice(list_file)
        try:
            bot.send_audio(i, au,"<a href=\'http://t.me/yupgrade_bot\'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺".format(message.from_user, bot.get_me()), parse_mode='html')
            num+=1
            print(num)
        except:
            pass
    print("Сообщение успешно отправлено")

    id = message.from_user.id
    name = message.from_user.first_name
    lastname = message.from_user.last_name
    username = message.from_user.username
    time = datetime.now()

    logFile = open("log/up/log.txt", "a")
    logFile.write(f"{time} | Пользователь отправил сообщение: @{id} {name} {lastname} {username} \n ")
    logFile.close()
    print(f'Сообщение №{id_voice} отправлена')
    plus_id = int(id_voice)
    result_id = plus_id + 1
    str_id = str(result_id)
    voice = open('info/voice.txt', 'a')
    voice.write('\n' + str_id)
    voice.close()
    print(f'Следующий номер сообщений №{str_id}')


# ________________________________________________________________________________________

# CHECK BOT ↓ TEST BOT ↓ TEST CMD ↓ TEST ZONE ↓ TEST CODE ↓ CHECK BOT ↓ TEST BOT ↓ TEST CMD ↓ TEST ZONE ↓ TEST  иCODE
@bot.message_handler(commands=['testbot'])
def testbot(message):
    bot.send_message(message.chat.id, "Бот работает\nНе парься УЛЫБНИСЬ :)")
    print("Бот работает :D")


@bot.message_handler(commands=['asendnewpost'])
def infopost(message):
    for i in joinedUsers:
        try:
            bot.send_message(i, "Дорогой человек, ежедневно мы трудимся над созданием и улучшением наших проектов, которые вдохновляют и мотивируют многих из Вас. Все голосовые, которые Вы слышите - это записывает живой человек, а не какой-либо бот.\n\nБот «Твой Апгрейд» - это лишь удобная площадка, через которую можно делать рассылку всем Вам. Чтобы содержать данного бота, мы ежемесячно его оплачиваем.\n\nЕсли Вы хотите поддержать наш труд финансово, можете выбрать любую удобную платежную систему и сделать перевод через - @yudonat_bot\n\n<b>Все ваши донаты пойдут на новое оборудование и на расширение наших проектов.</b>".format(message.from_user, bot.get_me()), parse_mode='html')
        except:
            pass
    print("Сообщение успешно отправлено_", message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)


# @bot.message_handler(commands = ['asendmessage'])
# def yousendmessage(message):
#     for i in joinedUsers:
#         try:#STOP STOP STOP STOP НАДО ДОРАБОТАТЬ ТЕКСТ!!!!!!!!!!!!!!!
#             bot.send_message(i, "Друзья скоро выйдет новое обновление!\n\n<a href=\'http://t.me/yupgrade_bot\'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺".format(message.from_user, bot.get_me()), parse_mode='html')
#             print("Сообщение успешно отправлено_", message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
#         except:
#             pass
@bot.message_handler(content_types=["file"])
def voice_cmd(message):
        # Узнаем id, если требуется
        id_voice = message.auido.file_id
        print(id_voice) # Вывод id сообщения в консоль
        # Отправка нужного аудио
        #bot.send_message(message.chat.id, str(id_voice))
# CHECK BOT ↑ TEST BOT ↑ TEST CMD ↑ TEST ZONE ↑ TEST CODE ↑ CHECK BOT ↑ TEST BOT ↑ TEST CMD ↑ TEST ZONE ↑ TEST CODE
@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.chat.type == 'private':
        if message.text == 'podcast':
            if not str(message.chat.id) in joinedUsers:
                podcastFile = open("log/podcast/id.txt", "a")
                podcastFile.write(str(message.chat.id) + '\n')
                podcastUsers.add(message.chat.id)

            id = message.from_user.id
            first_name = message.from_user.first_name
            last_name = message.from_user.last_name
            username = message.from_user.username
            time = datetime.now()
            podcastUsersFile = open("log/podcast/users.txt", "a")
            podcastUsersFile.write(f"{time} | Пользователь : @{id} {first_name} {last_name} {username} \n ")
            podcastUsersFile.close()
            bot.send_message(message.chat.id, "Отлично, вас добавили в список участников которые хотят слушать подкасы :)".format(message.from_user), parse_mode='html')



# Run bot
# bot.polling(none_stop=True)
def start_bot():
    if __name__ == '__main__':
        bot.polling(none_stop=True)
while True:
    try:
        start_bot()
    except:
        continue
    break