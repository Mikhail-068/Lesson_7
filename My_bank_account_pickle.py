"""
Программа Мой банковский счет
"""
import json
import os
import pickle
import yaml

text = '''
======== V I S A =========
  1. Посмотреть баланс.
  2. Пополнить счёт.
  3. Снять со счёта.
  4. Добавить покупку.
  5. История покупок.
  0. Выход.
--------------------------
'''

text_json = '''
------ И С Т О Р И Я   П О К У П О К -------
--------------------------------------------
|       У вас пока что нет покупок         |   
--------------------------------------------
'''.strip()

example_test = 'У вас пока что нет покупок'

file_name = 'balance.data'
file_buy = 'buy.json'

# Если нет файла balance.txt, мы его создаем и записыаем туда баланс = 0
if not os.path.exists(file_name):
    balance = {'balance': 0}
    with open(file_name, 'wb') as f:
        pickle.dump(balance, f)
if not os.path.exists(file_buy):
    with open(file_buy, 'w') as f:
        json.dump(text_json, f)


def read_():
    '''
    Функция для чтения баланса из нашего файла
    :return: словарь!
    '''
    with open(file_name, 'rb') as f:
        balance = pickle.load(f)

    return balance


def write_(balance):
    '''
    Записываем значение словаря!
    :param balance: словарь
    :return:
    '''

    with open(file_name, 'wb') as f:
        pickle.dump(balance, f)


def bank():
    while True:
        print(text)
        user = input('Введите номер: ')
        if user == '1':
            bal = read_()
            print(bal)

        elif user == '2':
            check = int(input('На сколько вы хотите пополнить счёт: '))
            bal = read_()
            bal['balance'] += check
            write_(bal)

        elif user == '3':
            check2 = int(input('Сколько вы хотите снять со счёта?: '))
            bal = read_()
            if check2 > bal['balance']:
                print('На вашем счёте не достаточно средств...')
            else:
                bal['balance'] -= check2
                write_(bal)

        elif user == '4':
            bue = input('Добавить покупку: ')





        elif user == '0':
            break
        else:
            continue


def read_json():
    with open(file_buy, 'r') as f:
        buy = json.load(f)
    return buy


# history = read_json()

file_buy2 = '1.yaml'
def write_json(buy, selector):
    with open(file_buy, selector, encoding='utf-8') as f:
        json.dump(buy, f, ensure_ascii=False)


buy = {'Покупки': ['батон', 'колбаса', 'майонез']}
# Проверяем, пустой список или нет.
# if example_test in history:
#     write_json(buy, 'w', encoding='utg-8')

write_json(buy, 'w')
