import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6480737039:AAFf475pQ3Pe2ESj1jZ1fqZxzrRIybUjKFg')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open game', web_app=WebAppInfo(url='https://mario-16zr.onrender.com/')))
    await message.answer('Hello, my friend!', reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer("Your score is "+ str(res["score"]))
    print("Send")

executor.start_polling(dp)