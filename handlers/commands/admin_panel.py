from utils.db_api.db_api import DataBaseManager
from states.states import StatesGroup
from data.config import IS_ADMIN
from aiogram import types
from loader import dp

@dp.message_handler(commands=['Get_UsersDataBase'])
async def get_data_base(message: types.Message):
    if await IS_ADMIN(message.chat.id):
        DataBaseManagerObject = DataBaseManager()
        await DataBaseManagerObject.connect("users_logs")
        db = await DataBaseManagerObject.get_info("*", "users")
        await DataBaseManagerObject.disconnect()
        del DataBaseManagerObject
        await message.answer(db)
    else:
        await message.answer("У вас нет на это прав ;)")

@dp.message_handler(commands=['Get_LogsDataBase'])
async def get_data_base(message: types.Message):
    if await IS_ADMIN(message.chat.id):
        DataBaseManagerObject = DataBaseManager()
        await DataBaseManagerObject.connect("users_logs")
        db = await DataBaseManagerObject.get_info("*", "logi")
        await DataBaseManagerObject.disconnect()
        del DataBaseManagerObject
        await message.answer(db)
    else:
        await message.answer("У вас нет на это прав ;)")
