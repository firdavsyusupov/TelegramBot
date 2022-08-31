from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btnUrlChannel = InlineKeyboardButton(text='ОБНОВИТЬ', url='https://t.me/firdavs_yusupov_official')
btnUpdate = InlineKeyboardButton(text='ОБНОВИТЬ', callback_data='updatebot')

update = InlineKeyboardMarkup(row_width=1)
#checkSubMenu.insert(btnUrlChannel)
update.insert(btnUpdate)


btnIrregularVerbs = InlineKeyboardButton(text='Неправильные глаголы английского языка', callback_data='irregularverbs')

startGameMenu = InlineKeyboardMarkup(row_width=1)
startGameMenu.insert(btnIrregularVerbs)