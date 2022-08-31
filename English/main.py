from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config
import logging
import markups as nav

logging.basicConfig(level=logging.INFO)
NOTSUB_MESSAGE = "Для доступа к боту, пожалуйста подпишитесь на канал!"
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


def check_sub(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


'''######################################-КЛИЕНТСКАЯ ЧАСТЬ-##############################################'''
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if check_sub(await bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Привет, "+message.chat.first_name + '!', reply_markup=nav.startGameMenu)
    else:
        await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)


@dp.callback_query_handler(text='subchanneldone')
async def subchannekdone(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    if check_sub(await bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Привет, "+message.chat.first_name + '!', reply_markup=nav.startGameMenu)
    else:
        await bot.send_message(message.from_user.id, 'Меня не обманишь!, Давай подпишись', reply_markup=nav.checkSubMenu)


@dp.callback_query_handler(text='irregularverbs')
async def irregularverbsgame(message: types.message):
    pass


@dp.message_handler()
async def talk(message: types.message):
    await bot.send_message(message.from_user.id, 'Пока что! Я В ас не понимаю :)')


while True:
    try:
        if __name__ == '__main__':
            executor.start_polling(dp, skip_updates=False)
    except:
        continue
    break
