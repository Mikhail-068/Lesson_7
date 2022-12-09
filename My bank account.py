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
    print(f'Ваш баланс: {balance}')

    return int(balance)




def write(new_balance):
    '''
    Записываем обязательно строковые данные!!!
    :param new_balance: str()
    :return:  None
    '''
    with open(file_name, 'w') as f:
        f.write(new_balance)












while True:
    print('1. Пополнить счёт')
    print('2. История покупок')
    print('2. История покупок')
    print('2. История покупок')
    print('3. Выход')
    choise = input('Введите номер: ')
    if choise == '1':
        name = input('Введите название: ')
        orders.append(name)
    elif choise == '2':
        for order in orders:
            print(order)
    elif choise == '3':
        with open(FILE_NAME, 'w') as f:
            for order in orders:
                f.write(f'{order}\n')
        break
    else:
        print('Неправильно введены даные')