from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter
from data.config import TEACHERS

class IsTeacher(BoundFilter):
    async def check(self, message: Message):
        return message.from_user.id in TEACHERS