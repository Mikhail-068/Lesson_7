"""
Программа Мой банковский счет
"""
import os, pickle

text = '''
======== V I S A =========
  1. Посмотреть баланс.
  2. Пополнить счёт.
  3. Снять со счёта.
  0. Выход.
--------------------------
'''
file_name = 'balance.data'


# Если нет файла balance.txt, мы его создаем и записыаем туда баланс = 0
if not os.path.exists(file_name):
    balance = {'balance': 0}
    with open(file_name, 'wb') as f:
        pickle.dump(balance, f)


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

# new_val = 15
#
# balance = read_()
# balance['balance'] += new_val
#
# write_(balance)
# print(read_())


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

        elif user == '0':
            break
        else:
            continue

bank()