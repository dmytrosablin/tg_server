import urllib.request
import requests

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6602794619:AAEspg2Ru9CL3XvUInibD_uVBrTLVepmpZc')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'play'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Open game', web_app=WebAppInfo(url="https://liltendo.onrender.com/")))
    await message.answer('Hello, my friend!', reply_markup=markup)

@dp.message_handler(commands=['record'])
async def record(message: types.Message):
    # contents = urllib.request.urlopen('https://liltendo.onrender.com/api/'+str(message.from_id)).read()
    contents = requests.get('https://liltendo.onrender.com/api/'+str(message.from_id))
    await message.answer('Your record is '+ contents.text)


@dp.message_handler(commands=['leaders'])
async def lider(message: types.Message):
    await message.answer("These are our leaders: ")
    contents = requests.get('https://liltendo.onrender.com/api/get_liders/123123').json()
    for i in range(len(contents)):
        await message.answer(contents[i]["record"])
@dp.message_handler()
async def echo(message: types.Message):
    print(message.text)
    await message.answer(message.text)


executor.start_polling(dp)
