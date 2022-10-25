from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import IS_HER
from data.config import IS_ADMIN
from loader import dp, bot
from utils.db_api.db_api import DataBaseManager


async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! \nЯ умею показывать картинки :)\nДля вашего же удобства, все картинки поделены по категориям\nВведите /category для отображения всех категорий")
    DataBaseManagerObject = DataBaseManager()
    await DataBaseManagerObject.connect("users_logs")
    await DataBaseManagerObject.add_new_info("users", "id, UserName", f"{message.chat.id}, '{message.from_user.username}'")
    await DataBaseManagerObject.disconnect()
    del DataBaseManagerObject
    if await IS_HER(message.chat.id) or await IS_ADMIN(message.chat.id):
        await dp.bot.set_my_commands([
            types.BotCommand("start", "Запуска бота"),
            types.BotCommand("help", "Помощь пользователю"),
            types.BotCommand("category", "Отображение доступных категорий"),
            types.BotCommand("for_u", ":)")])
    else:
        pass

