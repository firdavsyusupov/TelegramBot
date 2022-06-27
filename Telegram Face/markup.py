from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ---- Main Menu -----
btnreg = KeyboardButton('Regestrations')
btnlogin = KeyboardButton('Login')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnreg, btnlogin)

# ----- Log in -------
