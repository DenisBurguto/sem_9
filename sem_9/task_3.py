# Задание Nº3
# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат,
# который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json
import os.path
from functools import wraps


def my_dec_to_json(func):
    output_json = func.__name__ + ".json"
    if os.path.exists(output_json):
        with open(output_json, 'r', encoding='utf-8') as j_f:
            json_dic = json.load(j_f)
    else:
        json_dic = {}
    call = 1

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call

        json_dic[f'args {call=}'] = args

        for key, value in kwargs.items():
            json_dic[f'{key} {call=}'] = value
        result = func(*args, **kwargs)
        json_dic[f'result {call=} '] = result
        with open(output_json, 'w', encoding='utf-8') as j_f:
            json.dump(json_dic, j_f, indent=2)
        call += 1
        return result

    return wrapper


@my_dec_to_json
def my_func(*args, **kwargs):
    return [i ** power for i in args for power in kwargs.values()]


@my_dec_to_json
def sum_elements(*args):
    return sum(args)


if __name__ == '__main__':
    my_func(9, 333, power=2)
    my_func(5, power=4)
    my_func(88888, power=9)

    print(sum_elements(9, 333, 434))
    print(sum_elements(99, 33, 4))
