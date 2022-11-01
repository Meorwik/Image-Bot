from email import message
from data.config import IS_ADMIN, IS_HER, ADMINS
from aiogram.dispatcher import FSMContext
from states.states import StatesGroup
from aiogram import types
from loader import dp, bot
from codecs import open


@dp.message_handler(commands=['for_u'])
async def respond_on_special_command(message: types.Message):
    if await IS_HER(message.chat.id) or await IS_ADMIN(message.chat.id):
        await bot.send_message(text="Отправь боту любое сообщение ;)", chat_id=message.chat.id)
        await StatesGroup.stateInSpecialCommand.set()
    else:
        await message.answer(text="Упс =)\nПохоже эта функция не для вас)")


@dp.message_handler(state=StatesGroup.stateInSpecialCommand)
async def result_of_special_command(msg: types.Message, state: FSMContext):
    await bot.send_message(chat_id=int(ADMINS[0]), text=f"she sent: {msg.text}")
    with open("handlers/special_folder/for_her.txt", "r", 'utf-8') as file:
        line = file.read()
    await msg.answer(line)
    file.close()
    await bot.send_sticker(chat_id=msg.chat.id, sticker="CAACAgIAAxkBAAEY5qhjRa7uM0eh6b12vEasG2L95nUkIQACUAgAAkzMgErYSf6qHgzYgyoE")
    await state.finish()


@dp.message_handler(commands=['write_'])
async def some_spoecial_funk(message: types.Message):
    if await IS_ADMIN(message.chat.id):
        await StatesGroup.stateWritingDownSomeInfo.set()
        await message.answer("Ну что )\nПиши что хочeшь сказать )")
    else:
        pass
    
@dp.message_handler(state=StatesGroup.stateWritingDownSomeInfo)
async def write_file(msg: types.Message, state: FSMContext):
    with open("handlers/special_folder/for_her.txt", "w", 'utf-8') as file:
        file.write(msg.text)
    file.close()
    state.finish()