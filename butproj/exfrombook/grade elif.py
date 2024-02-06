his_name = input("Введите свое имя: ")

grade = int(input("Введите ваше кол-во баллов: "))
if grade >= 90:
    print("Ваша оценка: A")
elif grade >= 80:
    print("Ваша оценка: B")
elif grade >= 70:
    print("Ваша оценка: C")
elif grade >= 60:
    print("Ваша оценка: D")
else:
    print("Ваша оценка: F")
