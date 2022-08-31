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
        joined_file = open("log/up/joined.txt", "a")
        joined_file.write(str(message.chat.id
                              ) + '\n')
        joined_file.close()
        joinedUsers.add(message.chat.id)
    id_user = message.from_user.id
    name = message.from_user.first_name
    lastname = message.from_user.last_name
    username = message.from_user.username
    time = datetime.now()

    log_file = open("log/up/log.txt", "a")
    log_file.write(f"{time} | Пользователь запустил бота: {id_user} {name} {lastname} {username} \n ")
    log_file.close()

    users_data = open("log/up/users.txt", "a")
    users_data.write(f"{time} | ID: {id_user} | Name: {name} | Last name: {lastname} | Username: @{username} \n")
    users_data.close()


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
    logFile = open("log/up/log.txt", "a")
    logFile.write(f"{time} | Пользователь просматривает информацию: {id} {name} {lastname} {username} \n ")
    # logUsers.add(message.form_user.id)
    logFile.close()


@bot.message_handler(commands=['donat'])
def send_donat(message):
    bot.send_message(message.chat.id,
                     "Ежедневно мы трудимся над созданием и улучшением наших проектов, которые вдохновляют и мотивируют многих из Вас. Все голосовые которые Вы слышали или только услышите - это записываем мы лично, а не какой-либо бот."
                     "\n\nБот «Твой Апгрейд» - это лишь удобная площадка, через которую можно делать рассылку всем Вам. Чтобы содержать данного бота, мы ежемесячно его оплачиваем."
                     "\n\nЕсли Вы хотите поддержать наш труд финансово, можете выбрать любую удобную платежную систему и сделать перевод - @yudonat_bot"
                     "\n\n<b>Все ваши донаты пойдут на новое оборудование и на расширение наших проектов.</b>".format(
                         message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(commands=['help'])
def helpme(message):
    pass
    bot.send_message(message.chat.id, "У вас не работает бот?\n\n "
                                      " Варианты проблем:\n "
                                      " 1) Не приходят сообщения от бота - /errorsend\n\n "
                                      " Если у вас другая проблема пожалуйста свяжитесь с разработчиком - @firdavs_yusupov")

@bot.message_handler(commands=['errorsend'])
def error_send_message(message):
    id_user = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    time = datetime.now()

    filelog = open("log/up/errors.txt", "a")
    filelog.write(f"{time} | ОШИБКА отправка сообщение: {id_user} {name} {username}")
    filelog.close()
    bot.send_message(message.chat.id, "Ваша заявка принята, пожалуйста ожидайте ответа")


# New post for users_____________________________________________________________________
# SEND VOICE №25
@bot.message_handler(commands=['sendnewpost'])
def newpost(message):
    print('Ваше сообщение отправляется...')
    voice = open('info/voice.txt', 'r')
    id_voice = voice.readlines()[-1]
    voice.close()
    num = 0
    numb = 0
    print('Процесс...')
    for send in joinedUsers:
        au = open(f'info/{id_voice}.ogg', 'rb')
        # list_file = open['info/1.ogg', 'info/2.ogg','info/3.ogg','info/4.ogg','info/5.ogg']
        # ran = random.choice(list_file)
        try:
            bot.send_audio(send, au,
                           "<a href=\'http://t.me/yupgrade_bot\'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺".format(
                               message.from_user, bot.get_me()), parse_mode='html')
            num += 1
        except:
            numb += 1
    print("Сообщение успешно отправлено")
    allnum = num + numb
    print(f'Statistics:\nUser: {num}\nBlock: {numb}\nAll users: {allnum}')

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
    for apost in joinedUsers:
        try:
            bot.send_message(apost,
                             "Дорогой человек, ежедневно мы трудимся над созданием и улучшением наших проектов, которые вдохновляют и мотивируют многих из Вас. Все голосовые, которые Вы слышите - это записывает живой человек, а не какой-либо бот.\n\nБот «Твой Апгрейд» - это лишь удобная площадка, через которую можно делать рассылку всем Вам. Чтобы содержать данного бота, мы ежемесячно его оплачиваем.\n\nЕсли Вы хотите поддержать наш труд финансово, можете выбрать любую удобную платежную систему и сделать перевод через - @yudonat_bot\n\n<b>Все ваши донаты пойдут на новое оборудование и на расширение наших проектов.</b>".format(
                                 message.from_user, bot.get_me()), parse_mode='html')
        except:
            pass
    print("Сообщение успешно отправлено_", message.from_user.id, message.from_user.first_name,
          message.from_user.last_name, message.from_user.username)


@bot.message_handler(commands=['channelpost'])
def channelpost(message):
    for u in joinedUsers:
        try:
            menu1 = telebot.types.InlineKeyboardMarkup()
            menu1.add(
                telebot.types.InlineKeyboardButton(text='ПОДПИСАТЬСЯ', url='https://t.me/firdavs_yusupov_official'))
            bot.send_message(u,
                             text='Привет дорогой человек! \nЯ открыл канал в котором буду публиковать новые проекты и рассказывать про свою жизнь, если интересно подпишись буду рад :)',
                             reply_markup=menu1)
        except:
            pass



@bot.message_handler(content_types=["file"])
def voice_cmd(message):
    # Узнаем id, если требуется
    id_voice = message.auido.file_id
    print(id_voice)  # Вывод id сообщения в консоль
    # Отправка нужного аудио
    # bot.send_message(message.chat.id, str(id_voice))


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
            bot.send_message(message.chat.id, "В разрабодке...".format(message.from_user), parse_mode='html')


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
