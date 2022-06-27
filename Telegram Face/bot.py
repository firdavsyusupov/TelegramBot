import config
import aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types
import markup as nav

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await bot.send_message(message.from_user.id, 'Hello, you are welcomed by the FaceID bot :)\n'
                                                 'For further work, you need to register.'.format(message.from_user), reply_markup= nav.mainMenu)

@dp.message_handler()
async def regis(message: types.message):
    if message.text == 'Regestrations':
        await bot.send_message(message.from_user.id, )



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)