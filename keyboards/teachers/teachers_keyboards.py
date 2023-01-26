from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mp_th_start = InlineKeyboardMarkup()
mp_th_start.add(InlineKeyboardButton('Сделать объявление 📢', callback_data='make_announcement'))
mp_th_start.add(InlineKeyboardButton('Ответить на обращения ✉️', callback_data='ans_quations'))
