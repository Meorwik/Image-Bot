from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Команды: ",
            "/start - Запустить бота",
            "/help - Показать все команды",
            "/category - Показать все категории")
    await message.answer("\n".join(text))