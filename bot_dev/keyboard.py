from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatActions, ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from db import create_or_get_user
from db import create_box, get_user_boxes, delete_box

from db import get_overdue_boxes, get_all_boxes, get_box


def choose_role():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='🤵 Войти как администратор', callback_data='admin'),
        types.InlineKeyboardButton(text='🛒 Войти как заказчик', callback_data='user')
    ]
    keyboard.add(*buttons)
    return keyboard


def back():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


def kb1():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='*️⃣ Поддержка', callback_data='support'),
        types.InlineKeyboardButton(text='❓ F.A.Q', callback_data='faq'),
        types.InlineKeyboardButton(text='🎒 Забрать вещи', callback_data='get_back'),
        types.InlineKeyboardButton(text='✍ Оставить заявку', callback_data='application'),
        types.InlineKeyboardButton(text='📦 Мои боксы', callback_data='my_boxes'),
    ]
    keyboard.add(*buttons)
    return keyboard


def kb2():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='📩 Обратиться в поддержу', callback_data='letter_to_sup'),
        types.InlineKeyboardButton(text='🎒 Забрать вещи', callback_data='get_back'),
        types.InlineKeyboardButton(text='📦 Мои боксы', callback_data='my_boxes'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


def kb3():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='❌ Отменить', callback_data='cancel'),
        types.InlineKeyboardButton(text='🔧 Забрать курьером', callback_data='by_runner'),
        types.InlineKeyboardButton(text='🚙 Заберу лично', callback_data='by_myself'),
    ]
    keyboard.add(*buttons)
    return keyboard


def kb4():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='📦 Оставить вещи', callback_data='application'),
        types.InlineKeyboardButton(text='🎒 Забрать вещи', callback_data='get_back')
    ]
    keyboard.add(*buttons)
    return keyboard


def kb5():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='✅ Что можно хранить на складе', callback_data='storage_list'),
        types.InlineKeyboardButton(text='✍ Оставить заявку', callback_data='application'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')

    ]
    keyboard.add(*buttons)
    return keyboard


def kb6():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='✍ Оставить заявку', callback_data='application'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu'),
    ]
    keyboard.add(*buttons)
    return keyboard


def kb7():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='Подтвердить заказ', callback_data='ok'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


def boxes_main():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='Зимние вещи', callback_data='box1'),
        types.InlineKeyboardButton(text='Мебель', callback_data='furniture')
    ]
    keyboard.add(*buttons)
    return keyboard


def boxes2():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='🎒 Забрать вещи', callback_data='get_back_main'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


def choose_del():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='🔧 Бесплатная курьерская доставка', callback_data='runner'),
        types.InlineKeyboardButton(text='🚙 Отвезу сам', callback_data='myself'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu'),
        types.InlineKeyboardButton(text='❓ F.A.Q', callback_data='faq')
    ]
    keyboard.add(*buttons)
    return keyboard


def contact():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('📞 Отправить номер телефона',
                                                                            request_contact=True,
                                                                            one_time_keyboard=True))
    return keyboard


def choose_weight():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='до 10 кг', callback_data='ten'),
        types.InlineKeyboardButton(text='10-25 кг', callback_data='ten_twenty'),
        types.InlineKeyboardButton(text='40 - 70 кг', callback_data='40_70'),
        types.InlineKeyboardButton(text='70 - 100 кг', callback_data='70-100'),
        types.InlineKeyboardButton(text='более 100 кг', callback_data='more100'),
        types.InlineKeyboardButton(text='Не знаю, помогите мне!', callback_data='idk'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


def choose_height():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='Менее 3 кв. м.', callback_data='less3'),
        types.InlineKeyboardButton(text='3 - 7 кв. м', callback_data='3-7m'),
        types.InlineKeyboardButton(text='7 - 10 кв. м', callback_data='7-10m'),
        types.InlineKeyboardButton(text='Не знаю, помогите мне!', callback_data='idkh'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


def choose_data():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='1 месяц', callback_data='1'),
        types.InlineKeyboardButton(text='6 месяцев', callback_data='6'),
        types.InlineKeyboardButton(text='1 год', callback_data='1y'),
        types.InlineKeyboardButton(text='Другое', callback_data='other'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')

    ]
    keyboard.add(*buttons)
    return keyboard


def data_processing():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='Да', callback_data='yes'),
        types.InlineKeyboardButton(text='Нет, прошу не использовать мои персональные данные', callback_data='no')
    ]
    keyboard.add(*buttons)
    return keyboard


