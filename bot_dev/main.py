import os
from dotenv import load_dotenv
import asyncio
from asyncio import sleep

import db
from keyboard import *

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentTypes

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, ContentTypeFilter
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.types import Contact

load_dotenv()
tg_token = os.getenv('TG_BOT_TOKEN')
bot = Bot(token=tg_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class D(StatesGroup):
    contact = State()
    make_order = State()


async def on_startup(_):
    pass


@dp.callback_query_handler(text='storage_list')
async def send_good_list(call: types.CallbackQuery):
    good_list = """Что принимается на хранение:                                                                                                                              
✅ Мебель                             
✅ Бытовая техника                 
✅ Одежда и обувь                      
✅ Инструменты
✅ Посуда
✅ Книги
✅ Шины
✅ Велосипеды
✅ Мотоциклы и скутеры
✅ Спортивный инвентарь
Что не принимается на хранение:
❌ Алкоголь
❌ Продукты
❌ Деньги и драгоценности
❌ Изделия из натурального меха
❌ Живые цветы и растения
❌ Домашние питомцы
❌ Оружие и боеприпасы
❌ Взрывоопасные вещества и токсины
❌ Лаки и краски в негерметичной таре
❌ Любой мусор и отходы
    """
    await call.message.answer(good_list, reply_markup=next_keyboard())


@dp.callback_query_handler(text='support')
async def to_support(call: types.CallbackQuery):
    await call.message.answer('Выберите опцию:', reply_markup=support_buttons())


@dp.callback_query_handler(text='faq')
async def send_faq(call: types.CallbackQuery):
    faq = """
1. Оформите заявку, используя бота.
2. Мы рассчитаем подходящий тариф, исходя из объема вещей.
3. В удобное время к вам приедет команда муверов, упакует вещи, вынесет и отвезёт их на склад или на ваше новое место жительства.
4. Когда какая-то вещь снова понадобится, закажите возврат, и мы привезем её в любую точку Москвы.
5. Наша система не предусматривает дополнительных платежей за неиспользованное пространство. Это означает, \
что вы платите только за тот объем пространства, который фактически занимают ваши вещи, а не за весь объем комнаты для хранения.
6. Мы предлагаем услугу мобильного хранения, которая включает доставку наших профессиональных упаковочных материалов. \
Наша команда муверов соберет, упакует и маркирует все ваши вещи, а затем транспортирует их на наш склад. \
Все вещи хранятся на отдельных паллетах в надежных условиях. \
Наш склад постоянно контролируется видеокамерами без слепых зон, и круглосуточно охраняется.
7. Вы можете контролировать свои вещи через специальное меню нашего бота. \
Там вы можете заказать возврат вещей в любое удобное для вас время или добавить новые вещи для хранения. \
Все ваши вещи всегда находятся в безопасности и готовы к использованию.
    """
    await call.message.answer(faq, reply_markup=storage_list())


@dp.callback_query_handler(text='back_to_menu')
async def back_to_menu(call: types.CallbackQuery):
    await call.message.answer(text='Вы вернулись обратно в меню', reply_markup=main_keyboard())


@dp.callback_query_handler(text='application')
async def leave_a_request(call: types.CallbackQuery):
    await D.contact.set()
    await call.message.answer('Для продолжения нажмите кнопку ниже', reply_markup=request_keyboard())
    await asyncio.sleep(0.5)
    await call.message.answer('Укажите адрес, по которому нужно забрать вещи:')
    await asyncio.sleep(0.5)


@dp.callback_query_handler(text=['runner', 'myself'])
async def delivery(call: types.CallbackQuery):
    if call.data == 'runner':
        await call.message.answer('Вы выбрали курьерскую доставку! Укажите вес ваших вещей:', reply_markup=choose_weight())
    elif call.data == 'myself':
        await call.message.answer('Вы привезете вещи сами. Укажите вес ваших вещей:', reply_markup=choose_weight())


@dp.callback_query_handler(text=['ten', 'ten_twenty', '40_70', '70-100', 'more100', 'idk'])
async def choose_w(call: types.CallbackQuery):
    if call.data == 'idk':
        await call.message.answer("""Конечно! Мы поможем вам рассчитать вес и высоту ваших вещей. 
Вы можете привезти вещи сами или мы пришлем к вам команду муверов, чтобы рассчитать рост и вес на месте.""",
                                  reply_markup=choose_del())
    else:
        await call.message.answer('Теперь укажите высоту ваших вещей:', reply_markup=choose_height())


@dp.callback_query_handler(text='letter_to_sup')
async def send_letter_to_sup(call: types.CallbackQuery):
    await call.message.answer("""Данные для обращения в поддержку:
storagebot@gmail.com
+79215897941""")
    await asyncio.sleep(1)
    await call.message.answer('Для продолжения воспользуйтесь кнопками из меню ниже 👇:', reply_markup=next_keyboard())


@dp.message_handler(state=D.contact)
async def make_application(msg: types.Message, state: FSMContext, content_types=ContentTypes.CONTACT):
    await msg.answer('Ваши контактные данные получены.\nВыберите подходящую опцию из меню ниже 👇:', reply_markup=choose_del())
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    text = """Добро пожаловать! 
Мы компания, предоставляющая малогабаритные ячейки для сезонного хранения вещей.
Например велосипеды, каяки, cнегоходы. 
Мы заберём ваши вещи на наш склад, сохраним и привезём обратно в любую точку Москвы.
Для выбора интересующего вас раздела воспользуйтесь кнопками из меню ниже 👇
        """
    await msg.answer(text, reply_markup=main_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)