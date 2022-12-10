import json
import xml
import yaml

# Объект -> сохраняем в строку
# строка -> объект

# xml
# json
# yaml

person = {
    'name': 'Max',
    'age': 10,
    'phones': ['8911', '73833'],
    '1': 'test'
}

# print('Начальный объект')
# print(person)
# print(type(person))
#
# result = json.dumps(person)
#
# print('В формате json')
# print(result)
# print(type(result))
#
# person_recovery = json.loads(result)
#
# print('Восстановленный объект')
# print(person_recovery)
# print(type(person_recovery))
#
# print(person == person_recovery)
#
# # Сохранение в файл
# with open('person.json', 'w') as f:
#     json.dump(person, f)
#
# with open('person.json', 'r') as f:
#     result = json.load(f)
#     print(result)
import yaml
from yaml.loader import  SafeLoader, BaseLoader, FullLoader, UnsafeLoader
'''
Для функции yaml.load() доступны четыре загрузчика:
    * BaseLoader: загружает все базовые скаляры YAML как строки.
    * SafeLoader: безопасно загружает подмножество YAML, в основном используется, если документ поступает из ненадежного источника.
    * FullLoader: загружает полный YAML, но избегает выполнения произвольного кода. По-прежнему представляет потенциальный риск при использовании для ненадежных входных данных.
    * UnsafeLoader: оригинальный загрузчик для ненадежных входных данных, обычно используется для обратной совместимости.
'''
# YAML
with open('person.yaml', 'w') as f:
    yaml.dump(person, f, allow_unicode=True)

with open('buy.yaml', 'r', encoding='utf-8') as f:
    result = yaml.load(f, Loader=FullLoader)
    print(result)
