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

text_add = '''
    У вас пока что нет покупок, не желаете добавить покупку?
----------------------------------------------------------------
1. Добавить покупку.
2. Отказаться.

'''.strip()

text_add2 = '''
        Добавим покупку?
----------------------------------
1. Добавить покупку.
2. Отказаться.

'''.strip()


example_test = 'У вас пока что нет покупок'

file_name = 'balance.data'
file_buy = 'buy.yaml'
text_yaml = {'Покупки': []}


# Если нет файла "balance.txt", мы его создаем.
if not os.path.exists(file_name):
    balance = {'balance': 0}
    with open(file_name, 'wb') as f:
        pickle.dump(balance, f)


# Если нет "buy.yaml", мы его создаем.
if not os.path.exists(file_buy):
    with open(file_buy, 'w', encoding='utf-8') as f:
        yaml.dump(text_yaml, f, allow_unicode=True)


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


def read_yaml():
    with open(file_buy, 'r', encoding='utf-8') as f:
        buy = yaml.load(f, Loader=yaml.loader.FullLoader)

    return buy


def write_yaml(buy):
    with open(file_buy, 'w', encoding='utf-8') as f:
        yaml.dump(buy, f, allow_unicode=True)





def add_buy():
    '''
    Читаем файл с историей покупок и добавляем туда новые покупки. Записываем файл.
    :return: None
    '''
    user = input('Введите покупки:\n')

    history = read_yaml()
    print(history)
    temp = history['Покупки']
    # print(temp)
    temp.append(user)
    history['Покупки'] = temp
    # print(history)
    write_yaml(history)

# with open(file_buy, 'r', encoding='utf-8') as f:
#     buy = yaml.load(f, Loader=yaml.loader.FullLoader)

# print(file_buy)
# add_buy()

# Проверяем, пустой список или нет.
# if example_test in history:
#     write_yaml()
