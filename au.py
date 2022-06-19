#TEXT
"\n\n<a href = 'http://t.me/yupgrade_bot'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺"\

.format(message.from_user, bot.get_me()), parse_mode='html'

#CMD for send new audio post
@bot.message_handler(commands = ['sendnewpost'])
def newpost(message):
    for i in joinedUsers:
        au = open('info/.ogg', 'rb')
        bot.send_audio(i, au, "\n\n<a href=\'http://t.me/yupgrade_bot\'>© Твой Апгрейд ♥</a> \n\nПоделись с друзьями 🥺".format(message.from_user, bot.get_me()), parse_mode='html')
        print("Сообщение успешно отправлено_", message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)

#LOG all info
    id = message.from_user.id
    name = message.from_user.first_name
    lastname = message.from_user.last_name
    username = message.from_user.username
    time = datetime.now()

    logFile = open("log.txt", "a")
    logFile.write(f"{time} | Пользователь : @{id} {name} {lastname} {username} \n ")
    logFile.close()