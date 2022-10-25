from email import message
from keyboards.inline.inline_keyboard_for_category_choosing import \
(
    init_keyboard, switch_page_on_back, switch_page_on_next
)
from keyboards.default.reply_keyboard import keyboard_continue_or_stop
from LowLevelModuls.process_user_input import ParserManager
from utils.parser.web_requests import CategoryDict
from data.config import IS_ADMIN, IS_HER, ADMINS
from utils.db_api.db_api import DataBaseManager
from .category import category_command_respond
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from ..vars_for_handlers.vars import *
from states.states import StatesGroup
from loader import dp, bot
from aiogram import types
from datetime import date
from codecs import open
from loader import log


@dp.callback_query_handler(text=["switch_page_on_next", "switch_page_on_back"], state=StatesGroup.stateChoosingCat)
async def page_buttons(call: types.CallbackQuery):
    if call.data == "switch_page_on_next":
        now_on_page = await switch_page_on_next()
    elif call.data == "switch_page_on_back":
        log.info('switch_page_on_back')
        now_on_page = await switch_page_on_back()
    else:
        now_on_page = 0
    new_keyboard = await init_keyboard(now_on_page)
    await call.message.edit_reply_markup(reply_markup=new_keyboard)


@dp.callback_query_handler(text=CategoryDict.keys(), state=StatesGroup.stateChoosingCat)
async def get_category_chosen_by_user(call: types.CallbackQuery):
    await set_temp_category(call.data)
    DataBaseManagerObject = DataBaseManager()
    await DataBaseManagerObject.connect("users_logs")
    await DataBaseManagerObject.add_new_info("logi", "user_id, date_time, command", f"{call.from_user.id}, {str(date.today())}, '{call.data}'")
    await DataBaseManagerObject.disconnect()
    del DataBaseManagerObject 
    await call.answer(f"Выбрана категория : {call.data}")
    text = f"Вы выбрали категорию: {call.data} =)\nА теперь введите количество желаемых картинок ;)"
    await bot.delete_message(message_id=await get_message_id_to_edit(), chat_id=call.from_user.id)
    await bot.send_message(chat_id=call.from_user.id, text=text)
    await StatesGroup.stateChoosingCount.set()


@dp.message_handler(state=StatesGroup.stateChoosingCount)
async def set_count(message: types.Message, state: FSMContext):
    ParserManagerObject = ParserManager()
    collected_data = await ParserManagerObject.get_returned_data(message=message)
    await ParserManagerObject.try_two_scenarios_block(data=collected_data)
    await state.finish()
    await message.answer("Хотите выбрать еще одну категорию ?", reply_markup=keyboard_continue_or_stop)
    await StatesGroup.stateContinueOrStop.set()


@dp.message_handler(Text(equals=["Да"]), state=StatesGroup.stateContinueOrStop)
async def reply_on_yes(message: types.Message, state: FSMContext):
    await message.answer("Как пожелаете =)", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await StatesGroup.stateChoosingCount.set()
    await category_command_respond(message)


@dp.message_handler(Text(equals=["Нет"]), state=StatesGroup.stateContinueOrStop)
async def reply_on_no(message: types.Message, state: FSMContext):
    await message.answer("Мы благодарны за то что вы используете нашего бота ;)", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(commands=['Get_DataBase'])
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


@dp.message_handler(commands=['for_u'])
async def respond_on_special_command(message: types.Message):
    await bot.send_message(text="Отправь боту любое сообщение ;)", chat_id=message.chat.id)
    await StatesGroup.stateInSpecialCommand.set()


@dp.message_handler(state=StatesGroup.stateInSpecialCommand)
async def result_of_special_command(msg: types.Message, state: FSMContext):
    if await IS_HER(msg.chat.id) or await IS_ADMIN(msg.chat.id):
        await bot.send_message(chat_id=int(ADMINS[0]), text=f"she sent: {msg.text}")
        with open("W:/for_her.txt", "r", 'utf-8') as file:
            line = file.read()
        await msg.answer(line)
        await bot.send_sticker(chat_id=msg.chat.id, sticker="вам не нада это =)")
        file.close()
        await state.finish()
    else:
        await state.finish()


@dp.message_handler(commands=['write_save'])
async def some_spoecial_funk(message: types.Message):
    await bot.send_message(text="Отправь боту любое сообщение ;)", chat_id=message.chat.id)
    await StatesGroup.stateInSpecialCommand.set()