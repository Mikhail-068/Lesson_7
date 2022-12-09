"""
Программа Мой банковский счет
"""
import os

text = '''
======== V I S A =========
  1. Посмотреть баланс.
  2. Пополнить счёт.
  3. Снять со счёта.
  0. Выход.
--------------------------
'''
file_name = 'balance.txt'


# Если нет файла balance.txt, мы его создаем и записыаем туда баланс = 0
if not os.path.exists(file_name):
    with open(file_name, 'w') as f:
        f.write('0')


def read_():
    '''
    Функция для чтения баланса из нашего файла
    :return: число!!!
    '''
    with open(file_name, 'r') as f:
        balance = f.read()

    return int(balance)


def write_(new_balance):
    '''
    Записываем обязательно строковые данные!!!
    :param new_balance: str()
    :return:  None
    '''
    new_balance = str(new_balance)
    with open(file_name, 'w') as f:
        f.write(new_balance)


def bank():
    while True:
        print(text)
        user = input('Введите номер: ')
        if user == '1':
            bal = read_()
            print(f'Ваш баланс: {bal} руб.')
        elif user == '2':
             check = int(input('На сколько вы хотите пополнить счёт: '))
             bal = read_()
             bal += check
             write_(bal)
        elif user == '3':
            check2 = int(input('Сколько вы хотите снять со счёта?: '))
            bal = read_()
            if check2 > bal:
                print('На вашем счёте не достаточно средств...')
            else:
                bal -=  check2
                write_(bal)
        elif user == '0':
            break
        else:
            continue

