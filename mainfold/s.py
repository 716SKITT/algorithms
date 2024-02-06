import random
import matplotlib


def duty():
    grades = []
    while True:
        try:
            type_grade = input('Введите оценку: ')

            if type_grade.upper() == 'N':
                break
            else:

                grade = int(type_grade)
                if not 0 <= grade <= 5:
                    print("Оценка должна быть числом от 0 до 5.")
                    continue
                grades.append(grade)
        except ValueError:
            print("Неправильный ввод! Введите числовое значение оценки.")
    if grades:
        total_grade = sum(grades) - min(grades)
        average = total_grade / (len(grades) - 1)
        print(average)
    else:
        print('govno)')


# if __name__ == '__main__':
#     duty()


def main():
    with open(r'D:\temps\butproj\workwithfiles\sales.txt', 'r', encoding='utf-8') as sales_file:
        lines = sales_file.readlines()
        numbers = [int(line.strip()) for line in lines]
        print(numbers)


# main()
def test1():
    list1 = [1, 2, 3, 4, 5]
    list2 = [item**2 for item in list1]
    print(list1)
    print(list2)


# test1()

def test2():
    test_list = ['Suka', 'Blya', 'Tupica']
    len_test = [len(s) for s in test_list]

    print(len_test)
    print(test_list)


# test2()
# list1 = [1, 20, 30, 40, 2, 3, 4, 5, 77]
# list2 = [item for item in list1 if item < 10]
# print(list2)


def test3():
    rows = 3
    clos = 4
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for r in range(rows):
        for c in range(clos):
            values[r][c] = random.randint(1, 100)
    print(values)


# test3()


def test4():
    values = []
    for r in range(0, 3):
        row_values = []
        for c in range(0, 4):
            row_values.append(0)
        values.append(row_values)
    print(values)


# test4()


def study():
    try:
        for i in range(1, 20+1):
            answer = str(input(f'Введите ответ на {i} вопрос: '))
    except ValueError:
        print('ValueError')
    with open(r'D:\temps\mainfold\answers.txt', 'r') as file:
        ai = file.readlines()
        print(ai)


study()