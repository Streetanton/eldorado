from aiogram import Bot, Dispatcher

from config import token

bot = Bot(token)
dp = Dispatcher()

if __name__ == '__main__':
	executor.start_polling(dp)