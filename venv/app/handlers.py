from aiogram import types, F, Router
from aiogram.filters import Command, CommandStart
import string
import random
import app.keyboards as kb

router = Router()
num = 0


@router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(text='aa', reply_markup=kb.main)


@router.message(Command('desc'))
async def desc_command(message: types.Message):
    await message.answer('Bot azazaza')
    await message.delete()


@router.message(Command('count'))
async def count_command(message: types.Message):
    global num
    await message.answer(f'Count: {num}')
    num += 1


@router.message(Command('help', 'lol'))
async def ans(message: types.Message):
    await message.answer('lol')


@router.message(F.photo)
async def photo(message: types.Message):
    await message.answer(f'ID photo {message.photo[-1].file_id}')


@router.message(Command('get_p'))
async def get_photo(message: types.Message):
    await message.answer_photo(photo='https://lubimec.info/wp-content/uploads/2015/09/cats-kids-lubimetc.info_.jpg')


@router.message(F.text == 'lolo')
async def cc_echo(message: types.Message):
    await message.answer('not lol')


@router.message()
async def check_zero(message: types.Message):
    if message.text.find('0') != -1:
        await message.answer('Yes')
    else:
        await message.answer('No')
