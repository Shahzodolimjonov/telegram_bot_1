from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

study_centers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Everest', callback_data='everest'),
            InlineKeyboardButton(text='Cambridge', callback_data='cambridge'),
            InlineKeyboardButton(text='Thompson', callback_data='thompson'),
            InlineKeyboardButton(text='Internation', callback_data='internation'),
        ],
        [
            InlineKeyboardButton(text='Roboticslab', callback_data='robot'),
            InlineKeyboardButton(text='Najot talim', callback_data='najot'),
            InlineKeyboardButton(text='PDP Academy', callback_data='pdp'),
        ],
    ],
    resize_keyboard=True
)
subjects = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="English", callback_data='english'),
            InlineKeyboardButton(text="IELTS", callback_data='ielts'),
            InlineKeyboardButton(text="Fizika", callback_data='fizika'),
            InlineKeyboardButton(text="Dasturlash", callback_data='dasturlash'),
            InlineKeyboardButton(text="Tarix", callback_data='tarix'),
            InlineKeyboardButton(text="<--- Orqaga", callback_data='cancel1')
        ],
    ],
    resize_keyboard=True
)

teachers = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Humoyun tog'o", callback_data='humoyun'),
            InlineKeyboardButton(text="Xurshid O'roqov", callback_data='xurshid'),
            InlineKeyboardButton(text="Ahmadjon Ergashev", callback_data='ahmadjon'),
            InlineKeyboardButton(text="Otaxon Abdullayev", callback_data='otaxon'),
            InlineKeyboardButton(text="Maxmud Suyunov", callback_data='maxmud'),
            InlineKeyboardButton(text="<--- Orqaga", callback_data='cancel2')
        ],
    ],
    resize_keyboard=True
)

