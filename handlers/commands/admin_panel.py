from utils.db_api.db_api import DataBaseManager, getting_info_from_the_same_databse
from aiogram.dispatcher import FSMContext
from states.states import StatesGroup
from data.config import IS_ADMIN
from aiogram import types
from loader import dp

@dp.message_handler(commands=['adminOn'])
async def switch_admin_mode(message: types.Message):
    if await IS_ADMIN(message.chat.id):
        await StatesGroup.stateAdminMode.set()
        await message.answer("adminModeActiveted")
    else: 
        await message.answer("У вас нет на это прав )")
        
@dp.message_handler(commands=['Get_UsersDataBase'], state=StatesGroup.stateAdminMode)
async def get_users_data_base(message: types.Message):
    DataBaseInfo = await getting_info_from_the_same_databse(db_name="users_logs", get_what="*", get_from="users")
    await message.answer(DataBaseInfo)


@dp.message_handler(commands=['Get_LogsDataBase'], state=StatesGroup.stateAdminMode)
async def get_users_logs_data_base(message: types.Message):
    DataBaseInfo = await getting_info_from_the_same_databse(db_name="users_logs", get_what="*", get_from="logi")
    await message.answer(DataBaseInfo)
    

@dp.message_handler(commands=['adminOff'], state=StatesGroup.stateAdminMode)
async def turn_admin_mode_off(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("exitAdminMode")