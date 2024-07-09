from aiogram import Bot, Dispatcher
import asyncio
from config import token
from app.handlers import router

bot = Bot(token)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

