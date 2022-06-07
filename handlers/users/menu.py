from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, user, InlineKeyboardMarkup, InlineKeyboardButton

from data.config import ADMINS
from data.text import json
from loader import dp, bot


@dp.callback_query_handler(text=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], user_id=ADMINS)
async def one(query: types.CallbackQuery):
    main_key = InlineKeyboardMarkup(
               inline_keyboard=[[
                   InlineKeyboardButton(text=f'Topshiriqni bajarish', url=f'{json["1"][0]}'),
                   InlineKeyboardButton(text=f'Holat {json["1"][1]}', callback_data='<1')
               ]])
    await query.answer()
    await query.message.answer(text=f"Bajarilish kerak bo'lgan topshiriq ", reply_markup=main_key)


@dp.callback_query_handler(text='<1', chat_id=ADMINS)
async def get_menu0(call: CallbackQuery):
    json['1'][1] = "🔓"
    main_key = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text=f'Topshiriqni bajarish', url=f'{json["1"][0]}'),
            InlineKeyboardButton(text=f'Holat {json["1"][1]}', callback_data='>1')
        ]])
    await call.answer(cache_time=2)
    await call.message.edit_text(text='Bajarilish kerak bo\'lgan topshiriq ', reply_markup=main_key)


@dp.callback_query_handler(text='>1', chat_id=ADMINS)
async def get_menu0(call: CallbackQuery):
    json['1'][1] = "🔒"
    main_key = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text=f'Topshiriqni bajarish', url=f'{json["1"][0]}'),
            InlineKeyboardButton(text=f'Holat {json["1"][1]}', callback_data='>1')
        ]])
    await call.answer(cache_time=2)
    await call.message.edit_text(text='Bajarilish kerak bo\'lgan topshiriq ', reply_markup=main_key)
