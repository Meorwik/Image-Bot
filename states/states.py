from aiogram.dispatcher.filters.state import State, StatesGroup


class StatesGroup(StatesGroup):
    stateChoosingCat = State()
    stateChoosingCount = State()
    stateContinueOrStop = State()
    stateInSpecialCommand = State()
