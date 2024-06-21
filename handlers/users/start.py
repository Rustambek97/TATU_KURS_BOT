from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from course.models import Student
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    # try:
    #     Student.objects.create(
    #         username = message.from_user.username,
    #         first_name = message.from_user.first_name,
    #         last_name = message.from_user.last_name,
    #         telegram_id = message.from_user.id,
    #     )
    # except Exception as e:
    #     print(e)


