from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.studycenterKeyboard import study_centers
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=study_centers)

