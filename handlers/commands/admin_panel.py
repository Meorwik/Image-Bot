from utils.db_api.db_api import DataBaseManager, getting_info_from_the_same_databse
from states.states import StatesGroup
from data.config import IS_ADMIN
from aiogram import types
from loader import dp


@dp.message_handler(commands=['Get_UsersDataBase'])
async def get_data_base(message: types.Message):
    if await IS_ADMIN(message.chat.id):
        DataBaseInfo = getting_info_from_the_same_databse(db_name="users_logs", get_what="*", get_from="users")
        await message.answer(DataBaseInfo)
    else:
        await message.answer("У вас нет на это прав ;)")

@dp.message_handler(commands=['Get_LogsDataBase'])
async def get_data_base(message: types.Message):
    if await IS_ADMIN(message.chat.id):
        DataBaseInfo = getting_info_from_the_same_databse(db_name="users_logs", get_what="*", get_from="logi")
        await message.answer(DataBaseInfo)
    else:
        await message.answer("У вас нет на это прав ;)")
