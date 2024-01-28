# Задание No4
# 📌 Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой функции.
from functools import wraps


def my_deco_with_count(count):

    def my_deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)

        return wrapper

    return my_deco


@my_deco_with_count(8)
def my_func(*args, **kwargs):
    '''printing somestars'''
    for i in args:
        print(f'*{" ":{i}}' * i)
        for items in kwargs.items():
            print(items)


if __name__ == '__main__':
    print(my_func(1, 2, 3, 4, 5, multtiple=3, multiple_2=5))

