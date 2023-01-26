from aiogram.types import CallbackQuery

from filters.is_student import IsStudent
from main import continue_dialog, dp

@dp.callback_query_handler(IsStudent(), text='quation')
async def quation_callback_handler(query: CallbackQuery):
    await query.message.delete()
    await query.message.answer('Что всем передать?')
    await query.message.delete()
    await continue_dialog()

@dp.callback_query_handler(IsStudent(), text='git_acc')
async def ans_quations_callback_handler(query: CallbackQuery):
    await query.message.delete()
    await query.message.answer('Название категории?')