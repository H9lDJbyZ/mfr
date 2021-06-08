#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item0 = store[lamp_code][0]
lamps_quantity0, lamp_price0 = lamps_item0['quantity'], lamps_item0['price']
print('Лампа -', lamps_quantity0, 'шт, стоимость', lamps_quantity0 * lamp_price0, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
table_code = goods['Стол']
table_item0 = store[table_code][0]
tables_quantity0, tables_price0 = table_item0['quantity'], table_item0['price']
table_item1 = store[table_code][1]
tables_quantity1, tables_price1 = table_item1['quantity'], table_item1['price']
tables_quantity = tables_quantity0 + tables_quantity1
tables_price = tables_price0 + tables_price1
print('Стол -', tables_quantity, 'шт, стоимость', tables_quantity * tables_price, 'руб')

coach_code = goods['Диван']
coach_item0 = store[coach_code][0]
coach_quantity0, coach_price0 = coach_item0['quantity'], coach_item0['price']
coach_item1 = store[coach_code][1]
coach_quantity1, coach_price1 = coach_item1['quantity'], coach_item1['price']
coach_quantity = coach_quantity0 + coach_quantity1
coach_price = coach_price0 + coach_price1
print('Диван -', coach_quantity, 'шт, стоимость', coach_quantity * coach_price, 'руб')

chair_code = goods['Стул']
chair_item0 = store[chair_code][0]
chair_quantity0, chair_price0 = chair_item0['quantity'], chair_item0['price']
chair_item1 = store[chair_code][1]
chair_quantity1, chair_price1 = chair_item1['quantity'], chair_item1['price']
chair_item2 = store[chair_code][2]
chair_quantity2, chair_price2 = chair_item2['quantity'], chair_item2['price']
chair_quantity = chair_quantity0 + chair_quantity1 + chair_quantity2
chair_price = chair_price0 + chair_price1 + chair_price2
print('Стул -', chair_quantity, 'шт, стоимость', chair_quantity * chair_price, 'руб')

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################
