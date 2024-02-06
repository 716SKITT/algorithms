for x in range(0, 1010, 10):
    print(x, end=' ', sep=' ')

accept = 'Y'
while accept == 'Y':
    value1 = float(input('Введите первое значение: '))
    value2 = float(input('Введите второе значение: '))
    itog = value1 + value2
    print(itog)
    accept = input("Введите Y, если хотите еще раз: ")
