from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.parser.web_requests import CategoryDict

keyboard_inline = InlineKeyboardMarkup(row_width=3)
on_page = 1


async def switch_page_on_next():
    global on_page
    on_page += 1
    if on_page >= 7:
        on_page = 1
    return on_page


async def switch_page_on_back():
    global on_page
    on_page -= 1
    if on_page <= 0:
        on_page = 7
    return on_page


async def clear_keyboard():
    global keyboard_inline
    keyboard_inline = InlineKeyboardMarkup(row_width=3)


async def create_and_add_next_button():
    button_next = InlineKeyboardButton(text="Далее", callback_data="switch_page_on_next")
    keyboard_inline.add(button_next)


async def create_and_add_back_button():
    button_back = InlineKeyboardButton(text="Назад", callback_data="switch_page_on_back")
    keyboard_inline.add(button_back)


async def create_and_add_page_buttons():
    await create_and_add_back_button()
    await create_and_add_next_button()


async def show_page(page: int):
    buttons = []
    await clear_keyboard()
    for key, value in CategoryDict.items():
        if value == page:
            button = InlineKeyboardButton(text=key, callback_data=str(key))
            buttons.append(button)
    keyboard_inline.add(*buttons)


async def init_keyboard(num):
    await show_page(num)
    await create_and_add_page_buttons()
    return keyboard_inline
