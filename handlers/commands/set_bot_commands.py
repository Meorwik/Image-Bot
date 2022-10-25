from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запуска бота"),
            types.BotCommand("help", "Помощь пользователю"),
            types.BotCommand("category", "Отображение доступных категорий")
        ]
    )
