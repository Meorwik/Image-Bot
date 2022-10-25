from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_continue_or_stop = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да"),
         KeyboardButton(text="Нет")]
    ], resize_keyboard=True
)