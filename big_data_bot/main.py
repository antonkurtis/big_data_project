import telebot
import config
from telebot import types
from datetime import date
from datetime import timedelta
import pandas as pd
from scripts.download_data import get_data
from scripts.scrs import *
from scripts.make_plots import *

get_data()

bot = telebot.TeleBot(config.token)

df_salary = pd.read_csv('data/avg_salary.csv')
df_disc = pd.read_csv('data/df_disc.csv')
df_reg = pd.read_csv('data/df_reg.csv')

df_disc['DT'] = pd.to_datetime(df_disc['DT']).dt.date
df_reg['DT'] = pd.to_datetime(df_reg['DT']).dt.date

today = date.today()
yesterday = today - timedelta(days=1)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Регулярная цена')
    btn2 = types.KeyboardButton('Акционная цена')
    markup.add(btn1, btn2)

    bot.send_message(
        message.chat.id,
        'Бот умеет показывать регулярные и акционные средние цены по категориям продуктов в выбранном городе на '
        'текущий день. А так же отражает эти цены в процентах от средней зарплаты в регионе',
        reply_markup=markup
    )
    bot.send_message(
        message.chat.id,
        'Выберите регулярную или акционную цену',
        reply_markup=markup
    )


@bot.message_handler(content_types=['text'])
def bot_answer(message):
    global price

    if message.chat.type == 'private':
        if message.text == 'Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Регулярная цена')
            btn2 = types.KeyboardButton('Акционная цена')
            markup.add(btn1, btn2)

            bot.send_message(
                message.chat.id,
                'Бот умеет показывать регулярные и акционные средние цены по категориям продуктов в выбранном городе '
                'на '
                'текущий день. А так же отражает эти цены в процентах от средней зарплаты в регионе',
                reply_markup=markup
            )
            bot.send_message(
                message.chat.id,
                'Выберите регулярную или акционную цену',
                reply_markup=markup
            )

        elif message.text == 'Регулярная цена':

            price = 'regular'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            lst_1, lst_2, lst_3 = make_button_lists(df_disc.city.unique().tolist())
            for (btn1, btn2, btn3) in zip(lst_1, lst_2, lst_3):
                markup.add(btn1, btn2, btn3)
            back = types.KeyboardButton('Назад')
            markup.add(back)

            msg = bot.send_message(message.chat.id, 'Выберите интересующий город',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, goods_check)

        elif message.text == 'Акционная цена':

            price = 'discount'

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            lst_1, lst_2, lst_3 = make_button_lists(df_disc.city.unique().tolist())
            for (btn1, btn2, btn3) in zip(lst_1, lst_2, lst_3):
                markup.add(btn1, btn2, btn3)
            back = types.KeyboardButton('Назад')
            markup.add(back)

            msg = bot.send_message(message.chat.id, 'Выберите интересующий город',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, goods_check)


def goods_check(message):
    global city

    if message.text == 'Назад':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Регулярная цена')
        btn2 = types.KeyboardButton('Акционная цена')
        markup.add(btn1, btn2)

        bot.send_message(
            message.chat.id,
            'Бот умеет показывать регулярные и акционные средние цены по категориям продуктов в выбранном городе на '
            'текущий день. А так же отражает эти цены в процентах от средней зарплаты в регионе',
            reply_markup=markup
        )
        bot.send_message(
            message.chat.id,
            'Выберите регулярную или акционную цену',
            reply_markup=markup
        )
    else:
        if price == 'regular':
            city = message.text

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            lst_1, lst_2, lst_3 = make_button_lists(df_reg.subcategoryName.unique().tolist())
            for (btn1, btn2, btn3) in zip(lst_1, lst_2, lst_3):
                markup.add(btn1, btn2, btn3)
            back = types.KeyboardButton('Назад')
            markup.add(back)

            msg = bot.send_message(message.chat.id, 'Выберите интересующий товар',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, goods_check_next)
        elif price == 'discount':
            city = message.text

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            lst_1, lst_2, lst_3 = make_button_lists(df_disc.subcategoryName.unique().tolist())
            for (btn1, btn2, btn3) in zip(lst_1, lst_2, lst_3):
                markup.add(btn1, btn2, btn3)
            back = types.KeyboardButton('Назад')
            markup.add(back)

            msg = bot.send_message(message.chat.id, 'Выберите интересующий товар',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, goods_check_next)


def goods_check_next(message):
    global goods

    if message.text == 'Назад':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Регулярная цена')
        btn2 = types.KeyboardButton('Акционная цена')
        markup.add(btn1, btn2)

        bot.send_message(
            message.chat.id,
            'Бот умеет показывать регулярные и акционные средние цены по категориям продуктов в выбранном городе на '
            'текущий день. А так же отражает эти цены в процентах от средней зарплаты в регионе',
            reply_markup=markup
        )
        bot.send_message(
            message.chat.id,
            'Выберите регулярную или акционную цену',
            reply_markup=markup
        )
    else:
        if price == 'regular':
            goods = message.text

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            # yes = types.KeyboardButton('Да')
            # no = types.KeyboardButton('Нет')
            markup.add( back)

            region = transfer_city_to_region(city)
            salary = int(''.join(i for i in df_salary.loc[df_salary['Регион'] == region]['2022'].
                                 tolist()[0] if i.isdigit()))

            try:
                result = df_reg.loc[
                    (df_reg.city == city) &
                    (df_reg.subcategoryName == goods) &
                    (df_reg.DT == yesterday)
                    ]['avg_price_regular_new'].tolist()[0]

                bot.send_message(
                    message.chat.id,
                    f'Вы выбрали регулярную цену в городе: {city} \n '
                    f'На группу товаров: {goods}. \n'
                    f'Средняя цена за кг. составляет: {round(result, 2)} руб.',
                    reply_markup=markup
                )
                bot.send_message(
                    message.chat.id,
                    f'Стоимость выбранного товара составляет {round((result / salary * 100), 2)}% от средней '
                    f'зарплаты в '
                    f'регионе',
                    reply_markup=markup
                )
            except:
                bot.send_message(
                    message.chat.id,
                    f'Вы выбрали регулярную цену в городе: {city} \n '
                    f'На группу товаров: {goods}. \n'
                    f'Цена на выбранный товар в городе {city} за текущую дату отсутствует, '
                    f'пожалуйста выберите другой товар',
                    reply_markup=markup
                )

            bot.send_message(
                message.chat.id,
                f'Средняя зарплата в регионе: {round(salary, 2)} руб.',
                reply_markup=markup
            )

            # msg = bot.send_message(message.chat.id, 'Отошлю графики, если нажать "Да"',
            #                        reply_markup=markup)
            # bot.register_next_step_handler(msg, send_plots)

        elif price == 'discount':
            goods = message.text

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            # yes = types.KeyboardButton('Да')
            # no = types.KeyboardButton('Нет')
            markup.add(back)

            region = transfer_city_to_region(city)
            salary = int(''.join(i for i in df_salary.loc[df_salary['Регион'] == region]['2022'].
                                 tolist()[0] if i.isdigit()))

            try:
                result = df_disc.loc[
                    (df_disc.city == city) &
                    (df_disc.subcategoryName == goods) &
                    (df_disc.DT == yesterday)
                    ]['avg_price_discount_new'].tolist()[0]

                bot.send_message(
                    message.chat.id,
                    f'Вы выбрали акционную цену в городе: {city} \n '
                    f'На группу товаров: {goods}. \n'
                    f'Средняя цена за кг. составляет: {round(result, 2)} руб.',
                    reply_markup=markup
                )
                bot.send_message(
                    message.chat.id,
                    f'Стоимость выбранного товара составляет {round((result / salary * 100), 2)}% от средней '
                    f'зарплаты в '
                    f'регионе',
                    reply_markup=markup
                )
            except:
                bot.send_message(
                    message.chat.id,
                    f'Вы выбрали акционную цену в городе: {city} \n '
                    f'На группу товаров: {goods}. \n'
                    f'Цена на выбранный товар в городе {city} за текущую дату отсутствует, '
                    f'пожалуйста выберите другой товар',
                    reply_markup=markup
                )

            bot.send_message(
                message.chat.id,
                f'Средняя зарплата в регионе: {round(salary, 2)} руб.',
                reply_markup=markup
            )

            # msg = bot.send_message(message.chat.id, 'Отошлю графики, если нажать "Да"',
            #                        reply_markup=markup)
            # bot.register_next_step_handler(msg, send_plots)


def send_plots(message):
    if message.text == 'Назад':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Регулярная цена')
        btn2 = types.KeyboardButton('Акционная цена')
        markup.add(btn1, btn2)

        bot.send_message(
            message.chat.id,
            'Бот умеет показывать регулярные и акционные средние цены по категориям продуктов в выбранном городе на '
            'текущий день. А так же отражает эти цены в процентах от средней зарплаты в регионе',
            reply_markup=markup
        )
        bot.send_message(
            message.chat.id,
            'Выберите регулярную или акционную цену',
            reply_markup=markup
        )

    elif message.text == 'Да':
        if price == 'regular':
            df = df_reg

            make_single_plot(df, city, goods, price)
            make_multi_plot(df, goods, price)

        elif price == 'discount':
            df = df_disc

            make_single_plot(df, city, goods, price)
            make_multi_plot(df, goods, price)

        splot = open('data/outputs/single_plot.png', 'rb')
        mplot = open('data/outputs/multi_plot.png', 'rb')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад')
        markup.add(back)

        bot.send_message(
            message.chat.id,
            'График цены на выбранный товар по дням в выбранном городе:',
            reply_markup=markup)
        bot.send_photo(message.chat.id, splot)

        bot.send_message(
            message.chat.id,
            'График цены на выбранный товар по дням во всех городах:',
            reply_markup=markup)
        bot.send_photo(message.chat.id, mplot)

    elif message.text == 'Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад')
        markup.add(back)

        bot.send_message(
            message.chat.id,
            'Возвращаюсь в начало',
            reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()
