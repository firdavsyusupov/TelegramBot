import sqlite3
from sqlite3 import Error
from time import sleep, ctime
import telebot
from telebot import types
import pandas as pd

bot = telebot.TeleBot('5483326295:AAGA6BUhZPFIVgA93Ql_Kql3i7Y2RTQNXUo')
id = str(id)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("кнопка")


    markup.add(item1)

    bot.send_message(message.chat.id, "Привет, {0.first_name} !".format(message.from_user), 
    reply_markup = markup)

@bot.message_handler (content_types = ["text"])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Бонус💣":
            bot.send_message(message.chat.id, "сообщение")


def post_sql_query(sql_query):
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
    try:
        cursor.execute(sql_query)
    except Error:
        pass
    result = cursor.fetchall()
    return result

def create_tables():
    users_query = '''CREATE TABLE IF NOT EXISTS USERS 
                    (user_id INTEGER PRIMARY KEY NOT NULL,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    reg_date TEXT);'''
    post_sql_query(users_query)

def register_user(user, username, first_name, last_name):
    user_check_query = f'SELECT * FROM USERS WHERE user_id = {user};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
     insert_to_db_query = f'INSERT INTO USERS (user_id, username, first_name,  last_name, reg_date) VALUES ({user}, "{username}", "{first_name}", "{last_name}", "{ctime()}");'
     post_sql_query(insert_to_db_query )

    create_tables()

f = open('output.txt', 'w')
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('select * from USERS')
while True:
    df = pd.DataFrame(cursor.fetchmany(1000))
    if len(df) == 0:
        break

else:
    df.to_txt(f, header=False)


f.close()
cursor.close()
connection.close()



bot.polling(none_stop = True)   