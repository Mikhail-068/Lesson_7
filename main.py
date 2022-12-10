import yaml
from My_bank_account_pickle import *
import os
import pickle
import json

example = {'Покупки': ['хлеб', 'молоко', 'килька', 'колбаса']}


def add_buy():
    history = read_yaml()

    if text_yaml['Покупки'] == history['Покупки']:
        user_select = input(f'{text_add}\n')
        if user_select == '1':
            user = input('Введите покупку: ').split(', ')
            history['Покупки'] = user
            write_yaml(history)
    else:
        user_select = input(f'{text_add2}\n')
        if user_select == '1':
            user = input('Введите покупку: ').split(', ')
            temp = history['Покупки']
            for i in user:
                temp.append(i)
            history['Покупки'] = temp
            write_yaml(history)


add_buy()
