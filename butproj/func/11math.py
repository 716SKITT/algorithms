import random 


def randint():
    f1 = random.randrange(100, 1000)
    f2 = random.randrange(100, 1000)
    print(' ', f1)
    print('+', f2)
    value(f1, f2)


def value(f1, f2):
    total = f1 + f2
    answer = int(input('Введите ответ: '))
    if answer == total:
        print('Ответ правильный')
    else:
        print('Ответ неверный')
        randint()


randint()