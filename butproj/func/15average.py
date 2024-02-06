def averages():
    f1 = int(input('Введите 1-ую оценку: '))
    f2 = int(input('Введите 2-ю оценку: '))
    f3 = int(input('Введите 3-ю оценку: '))
    f4 = int(input('Введите 4-ю оценку: '))
    f5 = int(input('Введите 5-ю оценку: '))
    av = [f1, f2, f3, f4, f5]
    calc_averages(av)


def calc_averages(av):
    calc = sum(av) / 5
    int(calc)
    print(calc)
    determine_grade(calc)


def determine_grade(calc_averages):
    if calc_averages >= 90:
        grade = 'A'
    elif 80 >= calc_averages >= 89:
        grade = 'B'
    elif 70 >= calc_averages >= 79:
        grade = 'C'
    elif 60 >= calc_averages >= 69:
        grade = 'D'
    else:
        grade = 'F'

    print(grade)

averages()