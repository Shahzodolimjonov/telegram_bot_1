from aiogram.dispatcher.filters.state import StatesGroup, State


class Registerstate(StatesGroup):
    login = State()
    password = State()
class Information(StatesGroup):
    fullName = State()
    age = State()
    email = State()
    phone = State()
    adress = State()
    picture = State()