import telebot
import config
bot = telebot.TeleBot(config.TOKEN)

joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

@bot.message_handler(commands=['start'])
def startJoin(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)

@bot.message_handler(commands=['sendnewpost'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message).text[message.text.find(' '):]

# Run bot
bot.polling(none_stop=True)