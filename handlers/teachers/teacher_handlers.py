from aiogram.types import CallbackQuery

from filters.is_teacher import IsTeacher
from main import continue_dialog, dp

@dp.callback_query_handler(IsTeacher(), text='make_announcement')
async def make_announcement_callback_handler(query: CallbackQuery):
    await query.message.delete()
    await query.message.answer('Что всем передать?')
    await query.message.delete()
    await continue_dialog()

@dp.callback_query_handler(IsTeacher(), text='ans_quations')
async def ans_quations_callback_handler(query: CallbackQuery):
    await query.message.delete()
    await query.message.answer('Обращения')