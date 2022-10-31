from aiogram import executor
from loader import dp
from handlers.tool_panels.notify_admins import on_startup_notify
from handlers.tool_panels.set_bot_commands import set_default_commands

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
