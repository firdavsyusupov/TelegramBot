from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btnUrlChannel = InlineKeyboardButton(text='ПОДПИСАТЬСЯ', url='https://t.me/firdavs_yusupov_official')
btnDoneSub = InlineKeyboardButton(text='ПОДПИСАЛСЯ', callback_data='subchanneldone')

checkSubMenu = InlineKeyboardMarkup(row_width=1)
checkSubMenu.insert(btnUrlChannel)
checkSubMenu.insert(btnDoneSub)


btnIrregularVerbs = InlineKeyboardButton(text='Неправильные глаголы английского языка', callback_data='irregularverbs')

startGameMenu = InlineKeyboardMarkup(row_width=1)
startGameMenu.insert(btnIrregularVerbs)