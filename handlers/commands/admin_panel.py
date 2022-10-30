from utils.db_api.db_api import DataBaseManager, getting_info_from_the_same_databse
from .set_bot_commands import set_default_commands
from aiogram.dispatcher import FSMContext
from states.states import StatesGroup
from data.config import IS_ADMIN, ADMINS
from aiogram import types
from loader import dp

async def set_admin_commands():
    await dp.bot.set_my_commands(
        commands=[
            types.BotCommand("adminon", "Запуска режима админа"),
            types.BotCommand("users_db", "База данных пользователей"),
            types.BotCommand("logs_db", "Отображение доступных категорий"),
            types.BotCommand("adminoff", "Выйти из режима админа")
        ], scope=types.bot_command_scope.BotCommandScopeChat(ADMINS[0])
    )

@dp.message_handler(commands=['adminOn'])
async def switch_admin_mode(message: types.Message):
    if await IS_ADMIN(message.chat.id):
        await StatesGroup.stateAdminMode.set()
        await set_admin_commands()
        await message.answer("adminModeActiveted")
    else: 
        await message.answer("У вас нет на это прав )")
        
@dp.message_handler(commands=['Users_db'], state=StatesGroup.stateAdminMode)
async def get_users_data_base(message: types.Message):
    DataBaseInfo = await getting_info_from_the_same_databse(db_name="users_logs", get_what="*", get_from="users")
    await message.answer(DataBaseInfo)


@dp.message_handler(commands=['Logs_db'], state=StatesGroup.stateAdminMode)
async def get_users_logs_data_base(message: types.Message):
    DataBaseInfo = await getting_info_from_the_same_databse(db_name="users_logs", get_what="*", get_from="logi")
    await message.answer(DataBaseInfo)
    

@dp.message_handler(commands=['adminOff'], state=StatesGroup.stateAdminMode)
async def turn_admin_mode_off(message: types.Message, state: FSMContext):
    await state.finish()
    await set_default_commands(dp=dp)
    await message.answer("exitAdminMode")