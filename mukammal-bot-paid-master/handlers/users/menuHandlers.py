import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.inline.studycenterKeyboard import subjects, teachers, study_centers
# from keyboards.inline.callback_data import course_callback, book_callback
# from keyboards.inline.inlineKeyboard import categoryMenu, coursesMenu, booksMenu, telegram_keyboard,algoritm_keyboard, courses
from loader import dp, bot
from states.states_group import Information


# @dp.message_handler(state=None)
# async def enter_fullname(message: types.Message):
#     await message.answer("Loginni kiriting.")
#     await Registerstate.login.set()
#
#
# @dp.message_handler(state=Registerstate.login)
# async def fullname(message: types.Message, state: FSMContext):
#     if message.text == 'ahmad':
#         await message.answer("Parolingizni kiriting.")
#         login = message.text
#         await Registerstate.next()
#     else:
#         await message.answer("Login xato.Iltimos qaytib urunib ko'ring.")
#
#
# @dp.message_handler(state=Registerstate.password)
# async def enter_yosh(message: types.Message, state: FSMContext):
#     if message.text == 'qwerty':
#         password = message.text
#         await message.answer("Ma'lumotlaringiz to'g'ri, o'zingiz uchun kerakli bo'limni tanlang.")
#         await Registerstate.next()
#     else:
#         await message.answer("Parolingiz xato.Iltimos qaytib urunib ko'ring.")
#
#     data = await state.get_data()
#     msg = "Ma'lumotlar\n "
#     login_name = data.get('login')
#     password_name = data.get('password')
#     msg += f"Login : {login_name}\n"
#     msg += f"Password : {password_name}\n"
#     await bot.send_message(chat_id=1436980559, text=msg)
#     await state.finish()

@dp.callback_query_handler(text='everest')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Fanni tanlang : ", reply_markup=subjects)


@dp.callback_query_handler(text='cambridge')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Fanni tanlang : ", reply_markup=subjects)


@dp.callback_query_handler(text='thompson')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Fanni tanlang : ", reply_markup=subjects)


@dp.callback_query_handler(text='internation')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Fanni tanlang : ", reply_markup=subjects)


@dp.callback_query_handler(text='robot')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Fanni tanlang : ", reply_markup=subjects)


@dp.callback_query_handler(text='najot')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Fanni tanlang : ", reply_markup=subjects)


@dp.callback_query_handler(text='pdp')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Fanni tanlang : ", reply_markup=subjects)


@dp.callback_query_handler(text="cancel1")
async def cancel_buying(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=study_centers)
    await call.answer()


@dp.callback_query_handler(text='english')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ustozni tanlang : ", reply_markup=teachers)


@dp.callback_query_handler(text='ielts')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ustozni tanlang : ", reply_markup=teachers)


@dp.callback_query_handler(text='fizika')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ustozni tanlang : ", reply_markup=teachers)


@dp.callback_query_handler(text='dasturlash')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ustozni tanlang : ", reply_markup=teachers)


@dp.callback_query_handler(text='tarix')
async def course_selection(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ustozni tanlang : ", reply_markup=teachers)


@dp.callback_query_handler(text="cancel2")
async def cancel_buying(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=subjects)
    await call.answer()

@dp.callback_query_handler(text="humoyun", state=None)
async def enter_fullname(call: CallbackQuery):
    await call.message.answer("Iltimos to'liq ism familyangizni kiriting.")
    await Information.fullName.set()


@dp.message_handler(state=Information.fullName)
async def fullname(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({'name': name})
    await message.answer("Iltimos yoshingizni kiriting.")
    await Information.next()


@dp.message_handler(state=Information.age)
async def enter_yosh(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data({'age': age})
    await message.answer("Iltimos emailingiz kiriting.")
    await Information.next()


@dp.message_handler(state=Information.email)
async def email(message: types.Message, state: FSMContext):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, message.text):
        email = message.text
        await state.update_data({'email': email})
        await message.answer("Telefon raqamingizni kiriting.")
        await Information.next()
    else:
        await message.answer("Emailingiz xato,iltimos to'g'ri email kiriting.")


@dp.message_handler(state=Information.phone)
async def phone(message: types.Message, state: FSMContext):
    regex = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
    if re.fullmatch(regex, message.text):
        phone = message.text
        await state.update_data({'phone': phone})
        await message.answer("Manzilingizni kiriting  \n Masalan : 28 Uchtepa,Toshkent")
        await Information.next()
    else:
        await message.answer("Telefon raqamingiz xato,iltimos qayta harakat qilib ko'ring.")


@dp.message_handler(state=Information.adress)
async def address(message: types.Message, state: FSMContext):
    adress = message.text
    await state.update_data({'adress': adress})
    await message.answer("Malumotlaringiz qabul qilindi.")
    await Information.next()

    data = await state.get_data()
    msg = "Ma'lumotlar\n "
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')
    phone = data.get('phone')
    adress = data.get('adress')
    msg += f"Full_Name : {name}\n"
    msg += f"Age : {age}\n"
    msg += f"E-mail : {email}\n"
    msg += f"Phone_number : {phone}\n"
    msg += f"Address : {adress}\n"
    await bot.send_message(chat_id=1436980559, text=msg)
    await state.finish()
