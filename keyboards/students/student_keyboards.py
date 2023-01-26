from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mp_st_start = InlineKeyboardMarkup()
mp_st_start.add(InlineKeyboardButton('Задать вопрос ❓', callback_data='quation'))
mp_st_start.add(InlineKeyboardButton('Привязать (изменить) аккаунт github 👤', callback_data='git_acc'))
