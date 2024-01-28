# Задание No5
# 📌 Объедините функции из прошлых задач.
# 📌 Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# 📌 Выберите верный порядок декораторов.
from task_2 import guess_num, game_rules
from task_3 import my_dec_to_json
from task_4 import my_deco_with_count


@my_deco_with_count(5)
@my_dec_to_json
@game_rules
def task_5(hidden_number, trying):
    return guess_num(hidden_number, trying)


if __name__ == '__main__':
    task_5(900, 2)
