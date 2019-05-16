#
# Чтобы передавать данные между функциями, модулями или разными системами
# используются форматы данных. Одним из самых популярных форматов является JSON.
#
# Напишите декоратор to_json, который можно применить к различным функциям,
# чтобы преобразовывать их возвращаемое значение в JSON-формат.
# Не забудьте про сохранение корректного имени декорируемой функции.
import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        answ = json.dumps(func(*args, **kwargs))
        print(answ)
        return answ
    return wrapped

@to_json
def get_dict():
    return {get_dict.__name__: [("test", 10.0, None), False, 1]}  # Возврат словаря

@to_json
def get_sum(a, b):
    return a + b # Возврат вычисления

@to_json
def get_list():
    return ["a", None, 142, "54\'", '""'] # Возврат кортежа

@to_json
def get_set():
    return (1, 2, 3, 10, 20) # Возврат списска

@to_json
def get_obj():
    return list(filter(bool, range(3)))# Возврат объекта

@to_json
def get_none():
    return None # Возврат None

get_dict()
get_sum(54, 56)
get_list()
get_obj()
get_none()
get_set()