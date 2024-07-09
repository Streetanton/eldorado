from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

cars = ['bmw', 'mers']
main = ReplyKeyboardMarkup(keyboard=[
	[KeyboardButton(text=cars[0])],
	[KeyboardButton(text='button 1'), KeyboardButton(text='botton 2')]
],
resize_keyboard=True,
input_field_placeholder='write ')

settings = InlineKeyboardMarkup(inline_keyboard=[
	[InlineKeyboardButton(text='youtube', url='https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4')]
])
