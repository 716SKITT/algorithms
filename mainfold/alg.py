import random


def week():
    weekly = []
    for i in range(1, 7+1):
        inp = int(input(f'Введите значение за день {i}: '))
        weekly.append(inp)
    print(f'Всего за неделю: {sum(weekly)}')


# week()

def year():
    yearly = []
    for i in range(1, 12+1):
        inp = int(input(f'Введите кол-во дождевых осадков за {i} месяц: '))
        yearly.append(inp)
    print('суммарное кол-во осадков: ', sum(yearly))
    print('среднее кол-во осадков: ', f'{sum(yearly) / len(yearly):.2f}')
    print('максимальное кол-во осадков: ', max(yearly))
    print('минимальное кол-во осадков: ', min(yearly))


# year()


def listed():
    user_list = []
    for el in range(1, 20+1):
        while True:
            try:
                user_input = int(input(f"Введите число {el}: "))
                user_list.append(user_input)
                break
            except ValueError:
                print(f'Ошибка')

    print('sum: ', sum(user_list))
    print('average: ', f'{sum(user_list) / len(user_list):.2f}')
    print('man: ', max(user_list))
    print('min: ', min(user_list))


# listed()
def numbers_list():
    list_by_user = []
    program_list = []

    while True:
        try:
            int_by_user = int(input('Введите число n: '))
            break
        except ValueError:
            print("Это не число, пожалуйста, введите число.")

    while True:
        user_input = input('Введите число, которое хотите добавить в список или пробел для завершения: ')
        if user_input == '':
            break  
        try:
            inp = int(user_input)
            list_by_user.append(inp)
        except ValueError:
            print("Это не число, пожалуйста, введите число.")

    for value in list_by_user:
        if value > int_by_user:
            program_list.append(value)

    print("Числа больше", int_by_user, ":", program_list)


def lo_shu_square():
    matrix = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]

    for row in matrix:
        print(row)

    first = sum(matrix[0])
    second = sum(row[-1] for row in matrix)

    print(f"Сумма первой строки: {first}")
    print(f"Сумма последнего столбца: {second}")


# lo_shu_square()


def is_digital():
    perem = 'asdfa'
    if any(char.isdigit() for char in perem):
        print('1')
    else:
        print('0')


is_digital()