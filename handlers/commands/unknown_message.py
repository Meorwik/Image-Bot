from loader import dp
from aiogram import types
from states.states import StatesGroup

#TODO: THIS #### IS NOT WORKING :(

@dp.message_handler(state=StatesGroup.stateContinueOrStop)
async def can_not_recognize(message: types.Message):
    await message.answer("Я не понимаю что вы от меня хотите =(")