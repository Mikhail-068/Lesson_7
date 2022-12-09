import os, shutil, keyboard, platform
from time import sleep

menu = '''---------------------------------------------------
=== Выберите нужный пункт ===
---------------------------------------------------
1. создать папку
2. удалить (файл/папку)
3. копировать (файл/папку)
4. просмотр содержимого рабочей директории
5. посмотреть только папки
6. посмотреть только файлы
7. просмотр информации об операционной системе
8. создатель программы
9. играть в викторину
10. мой банковский счет
11. смена рабочей директории 
0. выход
'''


def create_file(name, text):
    with open(f'{name}.txt', 'w', encoding='utf-8') as f:
        f.write(text)


def show_directory():
    my_directory = os.getcwd()
    path = f'PATH:  {my_directory}'
    print((len(path) + 1) * '-')
    print(path)
    print((len(path) + 1) * '-')
    lst = os.listdir(my_directory)
    for i in lst:
        if os.path.isfile(os.path.join(my_directory, i)):
            print('[FILE]', i)
        else:
            print('[DIR] ', i)
    print((len(path) + 1) * '-')


def show_directory_DIR():
    my_directory = os.getcwd()
    path = f'Path:  {my_directory}'
    print((len(path) + 1) * '-')
    print(path)
    print((len(path) + 1) * '-')
    lst = os.listdir(my_directory)
    for i in lst:
        if os.path.isdir(os.path.join(my_directory, i)):
            print('[DIR]', i)

    print((len(path) + 1) * '-')

def show_directory_FILE():
    my_directory = os.getcwd()
    path = f'Path:  {my_directory}'
    print((len(path) + 1) * '-')
    print(path)
    print((len(path) + 1) * '-')
    lst = os.listdir(my_directory)
    for i in lst:
        if os.path.isfile(os.path.join(my_directory, i)):
            print('[FILE]', i)

    print((len(path) + 1) * '-')

def select():
    '''
    "Консольный файловый менеджер"
    :return:
    '''
    while True:
        user = int(input(menu))

        # 1 Создание файла и папки
        if user == 1:
            num = int(input('1. Создать файл\n2. Создать папку\n'))
            if num == 1:
                name_file = input('Введите имя файла:\n')
                text_ = input('Создержимое файла:\n')
                create_file(name_file, text_)
            elif num == 2:
                name_folder = input('Введите имя папки:\n')
                os.mkdir(name_folder)

        # Удаление файла и папки
        elif user == 2:
            num = int(input('1. Удалить файл\n2. Удалить папку\n'))
            if num == 1:
                del_file = input('Введите имя файла:\n')
                os.remove(f'{del_file}')
            elif num == 2:
                del_folder = input('Введите имя папки:\n')
                shutil.rmtree(del_folder)

        # Копирование файла и папки
        elif user == 3:
            num = int(input('1. Копировать файл\n2. Копировать папку\n'))
            if num == 1:
                path, path2 = input('Откуда?\n'), input('Куда?\n')
                shutil.copy(path, path2)
            elif num == 2:
                path, path2 = input('Откуда?\n'), input('Куда?\n')
                shutil.copytree(path, f'{path2}/{path}')

        # Просмотр содержимого рабочей директории
        elif user == 4:
            show_directory()
            print('Для продолжения нажмите «Esc» ...')
            keyboard.wait('esc')

        # Посмотреть только папки
        elif user == 5:
            show_directory_DIR()
            print('Для продолжения нажмите «Esc» ...')
            keyboard.wait('esc')

        # Посмотреть только файлы
        elif user == 6:
            show_directory_FILE()
            print('Для продолжения нажмите «Esc» ...')
            keyboard.wait('esc')

        #  Инфо об операционной системе
        elif user == 7:
            print('-' * 30)
            print(platform.platform())
            print(*platform.architecture())
            print('-' * 30)
            print('Для продолжения нажмите «Esc» ...')
            keyboard.wait('esc')

        # Создатель программы
        elif user == 8:
            print('*********************')
            print('   == Mihail_AI ==   ')
            print('*********************')
            print('Для продолжения нажмите «Esc» ...')
            keyboard.wait('esc')

        # Викторина
        elif user == 9:
            vic()

        # Банковский счёт
        elif user == 10:
            print('----- C Б Е Р Б А Н К -------')
            print('0000 0000 0000 0000 0000 0000')
            print('-----------------------------')
            print('Для продолжения нажмите «Esc» ...')
            keyboard.wait('esc')

        # Смена рабочей директории (* дополнительно)
        elif user == 11:
            print('Наша директория:', os.getcwd())
            print(os.listdir(os.getcwd()))
            new_path = input('Введите новый путь: (Пример => «D:/»)\n')
            os.chdir(new_path)
            print('Наша директория:', os.getcwd())
            print(os.listdir(os.getcwd()))
            print('Для продолжения нажмите «Esc» ...')
            keyboard.wait('esc')
        else:
            break


if __name__ == '__main__':
    pass