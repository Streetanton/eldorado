'''import requests
import time
from config import token


API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
BOT_TOKEN = token
TEXT = 'Ура! Классный апдейт!'
MAX_COUNTER = 100

offset = 0
counter = 0
chat_id: int
timeout = 10
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1

'''
from config import token
from aiogram.filters import Command
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message

bot = Bot(token)
dp = Dispatcher()

async def start_command(message:Message):
    await message.answer("No start")


async def help_command(message:Message):
    await message.answer("No help")


async def photo_send(message:Message):
    await message.answer_photo(message.photo[-1].file_id)


#@dp.message(Command(F.audio))
async def voice_send(message:Message):
    await message.answer_voice(message.voice.file_id,caption='no voice')


async def echo_send(message:Message):
    await message.answer(message.text)



dp.message.register(start_command, Command(commands="start"))
dp.message.register(help_command, Command(commands="help"))
dp.message.register(photo_send, F.photo)
dp.message.register(voice_send, F.voice)
dp.message.register(echo_send)


def custom_filter(some_list: list) -> bool:
  return sum([num for num in some_list if isinstance(num, int) and num % 7 == 0]) < 83 or False


anonymous_filter = lambda strok: (strok.lower().count('я') >= 23)


if __name__ == '__main__':
    #dp.run_polling(bot)
    print(anonymous_filter('Я - последняя буква в алфавите!'))
    print(anonymous_filter('яяяяяяя яяяяяяя яяяяяяя яя,  тоже!'))
    print(anonymous_filter('яяяяяяя яяяяяяя яяяяяяя яяя,  тоже!'))