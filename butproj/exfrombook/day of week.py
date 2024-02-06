day = int(input("Введите день недели: "))
if day < 0 and day > 7:
    print("Введите от 1 до 7")
elif day == 1:
    print("Понедельник, день тяжелый...")
elif day == 2:
    print("Вторник")
elif day == 3:
    print("Среда")
elif day == 4:
    print("Четверг")
elif day == 5:
    print("Пятница")
elif day == 6:
    print("Суббота")
elif day == 7:
    print("Воскресенье")
else:
    print("Введите число в диапозоне от 1 до 7")