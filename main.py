import json
import logging
import os
from aiogram import Bot, Dispatcher, types

from data.config import TEACHERS
from keyboards.students.student_keyboards import mp_st_start
from keyboards.teachers.teachers_keyboards import mp_th_start
from handlers.teachers import teacher_handlers
from handlers.students import students_headers


# Logger initialization and logging level setting
log = logging.getLogger(__name__)
log.setLevel(os.environ.get('LOGGING_LEVEL', 'INFO').upper())

def setup(dp: Dispatcher, name_of_file):
    for i in [obj for (name , obj) in vars(name_of_file).items()
        if hasattr(obj, "__class__") and obj.__class__.__name__ == "function"]:
            dp.register_message_handler(i)

# Handlers
async def start(message: types.Message):
    await message.reply('Hello, {}!'.format(message.from_user.first_name), reply_markup=(mp_st_start, mp_th_start)[message.from_user.id in TEACHERS])

async def continue_dialog(message: types.Message):
    await message.reply('Что еще нужно сделать?', reply_markup=(mp_st_start, mp_th_start)[message.from_user.id in TEACHERS])

async def echo(message: types.Message):
    await message.answer(message.text)

# Functions for Yandex.Cloud
async def register_handlers(dp: Dispatcher):
    setup(dp, teacher_handlers)
    setup(dp, students_headers)
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(echo)

    log.debug('Handlers are registered.')


async def process_event(event, dp: Dispatcher):
    update = json.loads(event['body'])
    log.debug('Update: ' + str(update))

    Bot.set_current(dp.bot)
    update = types.Update.to_object(update)
    await dp.process_update(update)

async def handler(event, context):
    if event['httpMethod'] == 'POST':
        # Bot and dispatcher initialization
        bot = Bot(os.environ.get('TOKEN'))
        dp = Dispatcher(bot)

        await register_handlers(dp)
        await process_event(event, dp)

        return {'statusCode': 200, 'body': 'ok'}
    return {'statusCode': 405}
