import random


def main():
    a = random.randint(1, 100)
    b = int(input('write: '))
    while b != a:
        if b > a:
            print('Нужно меньше, попробуйте еще раз')
            b = int(input('write: '))
        elif b < a:
            print('Нужно больше, попробуйте еще раз')
            b = int(input('write: '))
    print('right!', a)


main()