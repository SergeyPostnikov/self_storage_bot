from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatActions, ReplyKeyboardMarkup, KeyboardButton
from aiogram import types


def kb_adm_back():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    button = [
        types.InlineKeyboardButton(text='◀️Обратно в меню', callback_data='adm_menu')
    ]
    return keyboard


def kb_admin_1():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='⌛️Просроченные боксы', callback_data='no_time'),
        types.InlineKeyboardButton(text='⏱Активные заказы', callback_data='active'),
        types.InlineKeyboardButton(text='🖇Рекламные ссылки', callback_data='ad'),
        types.InlineKeyboardButton(text='🗃Занятые боксы', callback_data='full_boxes')
    ]
    keyboard.add(*buttons)
    return keyboard


def kb_admin_2():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='➡️ Следующий бокс', callback_data='next_b'),
        types.InlineKeyboardButton(text='📋 Отобразить списком', callback_data='make_list'),
        types.InlineKeyboardButton(text='◀️ Обратно в меню', callback_data='adm_menu'),
    ]
    keyboard.add(*buttons)
    return keyboard


def kb_admin_3():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='➡️ Следующий заказ', callback_data='next_apl'),
        types.InlineKeyboardButton(text='📋 Отобразить списком', callback_data='make_order_list'),
        types.InlineKeyboardButton(text='☑️ Выполнить заказ', callback_data='take_order'),
        types.InlineKeyboardButton(text='◀️ Обратно в меню', callback_data='adm_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


def kb_admin_4():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='➡️ Следующий бокс', callback_data='next_full_b'),
        types.InlineKeyboardButton(text='📋 Отобразить списком', callback_data='make_list_b'),
        types.InlineKeyboardButton(text='◀️ Обратно в меню', callback_data='adm_menu'),
    ]


def choose_weight_adm():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='до 10 кг', callback_data='10'),
        types.InlineKeyboardButton(text='10-25 кг', callback_data='10-20'),
        types.InlineKeyboardButton(text='40 - 70 кг', callback_data='4-7'),
        types.InlineKeyboardButton(text='70 - 100 кг', callback_data='7-10'),
        types.InlineKeyboardButton(text='более 100 кг', callback_data='100'),
        types.InlineKeyboardButton(text='◀️ Обратно в меню', callback_data='adm_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


def choose_height_adm():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='Менее 3 кв. м.', callback_data='less_3'),
        types.InlineKeyboardButton(text='3 - 7 кв. м', callback_data='3-7'),
        types.InlineKeyboardButton(text='7 - 10 кв. м', callback_data='7-10'),
        types.InlineKeyboardButton(text='◀️ Обратно в меню', callback_data='adm_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


def choose_order_date():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='1 месяц', callback_data='month'),
        types.InlineKeyboardButton(text='6 месяцев', callback_data='sixmonth'),
        types.InlineKeyboardButton(text='1 год', callback_data='year'),
        types.InlineKeyboardButton(text='Другое', callback_data='diff'),
        types.InlineKeyboardButton(text='◀️ Обратно в меню', callback_data='adm_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


def accept_orde():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = [
        types.InlineKeyboardButton(text='Подтвердить заказ', callback_data='accept_ord'),
        types.InlineKeyboardButton(text='◀️ Обратно в меню', callback_data='adm_menu')
    ]
    keyboard.add(*button)
    return keyboard