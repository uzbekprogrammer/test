from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.main import main_key
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum , {message.from_user.full_name}!\nTopshiriqni tanlang!", reply_markup=main_key)
