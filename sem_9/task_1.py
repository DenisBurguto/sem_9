# Кирилл Панфилов 📌 Создайте функцию-замыкание, которая запрашивает
# два целых числа: ○ от 1 до 100 для загадывания, ○ от 1 до 10 для количества попыток 📌
# Функция возвращает функцию, которая через консоль
# просит угадать загаданное число за указанное число попыток.

def guess_num(hidden_number: int, trying: int = 1):
    def func():
        count = trying
        print(f'Hi. try to guess hidden number from 1 to 100. You have {count} tries only! ')
        while count:
            user_num = int(input(f'try #{trying-count+1}, make your choice: '))
            if user_num == hidden_number:
                print(f'Great! You win! Hidden number is {hidden_number}')
                exit(0)
            else:
                print(
                    f'Sorry, you are mistaken. Hidden number is {'>' if user_num < hidden_number else '<'} then yours')
            count -= 1

        print(f'You loose (: Hidden number was {hidden_number}')

    return func

if __name__ == '__main__':


    f = guess_num(50, 3)

    f()
