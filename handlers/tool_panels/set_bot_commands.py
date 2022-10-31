from aiogram import Bot, Dispatcher, types


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        commands=[
            types.BotCommand("start", "Запуска бота"),
            types.BotCommand("help", "Помощь пользователю"),
            types.BotCommand("category", "Отображение доступных категорий"),
            types.BotCommand("for_u", ":)")
        ], scope=types.bot_command_scope.BotCommandScopeDefault()
    )
