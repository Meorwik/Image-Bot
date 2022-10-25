from aiogram import types
from handlers.vars_for_handlers.vars import set_message_id_to_edit
from states.states import StatesGroup
from loader import dp
from keyboards.inline.inline_keyboard_for_category_choosing import init_keyboard


@dp.message_handler(commands=['category'])
async def category_command_respond(message: types.Message):
    message_ = await message.answer("Этот бот имеет в себе очень много разных категорий, вы можете выбрать любую из ниже перечисленных:", reply_markup=await init_keyboard(1))
    await set_message_id_to_edit(message_.message_id)
    await StatesGroup.stateChoosingCat.set()
