
NUM_EMPLOYEES = 6

def pay():
    hours = [0] * NUM_EMPLOYEES  

    for index in range(NUM_EMPLOYEES):
        hours[index] = float(input(f'Введите число отработанных часов сотрудником {index + 1}: '))

    pay_rate = float(input('Введите почасовую ставку оплаты: '))

    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print(f'Зарплата сотрудника {index + 1}: ${gross_pay:,.2f}')

#pay()

def main():
    numbers = [2, 3, 42, 10, 2]
    print(f'Сумма списка: {averages(numbers)}')


def averages(numbers):
    return sum(numbers)

#main()

def duty():
    grades = []
    while True:
        try:
            typegrade = input('Введите оценку: ')

            if typegrade.upper() == 'N':
                break
            else:

                grade = int(typegrade)
                if not 0 <= grade <= 100:
                    print("Оценка должна быть числом от 0 до 100.")
                    continue
                grades.append(grade)
        except ValueError:
            print("Неправильный ввод! Введите числовое значение оценки.")
    if grades:  
        total_grade = sum(grades) - min(grades)
        average = total_grade / (len(grades)-1)
        print(average)
    else:
        print('govno)')

duty()


def gptduty():
    grades = []

    print("Введите все оценки. Для окончания введите 'N'.")

    while True:
        try:
            grade_input = input('Введите оценку (или N для завершения): ')

            if grade_input.upper() == 'N':
                break
            else:

                grade = int(grade_input)
                if not 0 <= grade <= 100:
                    print("Оценка должна быть числом от 0 до 100.")
                    continue
                grades.append(grade)
        except ValueError:
            print("Неправильный ввод! Введите числовое значение оценки.")

    if grades:
        total_without_min = sum(grades) - min(grades)
        average = total_without_min / (len(grades) - 1)
        print(f'Средняя оценка с учетом удаления минимальной: {average:.2f}')
    else:
        print("Оценки не были введены.")

#gptduty()
