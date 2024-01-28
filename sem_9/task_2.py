# Задание No2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию- угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.
from random import randint
from functools import wraps

MIN_NUM = 1
MAX_NUM = 100
MIN_TRY = 1
MAX_TRY = 10


def game_rules(func):
    @wraps(func)
    def wrapper(hidden_number, trying):
        hidden_number = hidden_number if MIN_NUM <= hidden_number <= MAX_NUM else randint(MIN_NUM, MAX_TRY)
        trying = trying if MIN_TRY <= trying <= MAX_TRY else randint(MIN_TRY, MAX_TRY)
        res = func(hidden_number, trying)
        return res

    return wrapper


@game_rules
def guess_num(hidden_number, trying):
    count = trying
    print(f'Hi. try to guess hidden number from {MIN_NUM} to {MAX_NUM}. You have {count} tries only! ')
    while count:
        user_num = int(input(f'try #{trying - count + 1}, make your choice: '))
        if user_num == hidden_number:
            print(f'Great! You win! Hidden number is {hidden_number}')
            return f'WIN! -hidden_number: {hidden_number}'
        else:
            print(
                f'Sorry, you are mistaken. Hidden number is {'>' if user_num < hidden_number else '<'} then yours')
        count -= 1

    print(f'You loose (: Hidden number was {hidden_number}')
    return f'LOOSE!-hidden_number: {hidden_number}'


if __name__ == '__main__':
    print(guess_num(50, 3))
