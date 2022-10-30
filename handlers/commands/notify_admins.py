from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from data.config import ADMINS
from handlers.commands.start import bot_start


async def on_startup_notify():
    for admin in ADMINS:
        await dp.bot.send_message(admin, "Бот успешно запустился !")

@dp.message_handler(CommandStart())
async def who_used_my_bot_notify(message: types.Message):
    for admin in ADMINS:
        await dp.bot.send_message(admin, f"Бот запущен юзером: {message.from_user.username}")
        await bot_start(message)
