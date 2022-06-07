from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.text import json

main_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Exercise 1️⃣", callback_data='1'),
            InlineKeyboardButton(text="Exercise 2️⃣", callback_data='2'),
            InlineKeyboardButton(text="Exercise 3️⃣", callback_data='3'),
        ],
        [
            InlineKeyboardButton(text="Exercise 4️⃣", callback_data='4'),
            InlineKeyboardButton(text="Exercise 5️⃣", callback_data='5'),
            InlineKeyboardButton(text="Exercise 6️⃣", callback_data='6'),
        ],
        [
            InlineKeyboardButton(text="Exercise 7️⃣", callback_data='7'),
            InlineKeyboardButton(text="Exercise 8️⃣", callback_data='8'),
            InlineKeyboardButton(text="Exercise 9️⃣", callback_data='9'),
        ],
        [
            InlineKeyboardButton(text="Exercise 🔟", callback_data='10'),
        ]
    ]
)