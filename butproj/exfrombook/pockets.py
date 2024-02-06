pockets = int(input("Введите номер кормана: "))
if pockets == 0:
    print("Зеленый")
elif pockets >= 1 and pockets <= 10:
    if pockets % 2:
        print("Черный")
    else:
        print("Красный")
elif pockets >= 11 and pockets <= 18:
    if pockets % 2:
        print("Красный")
    else:
        print("Черный")
elif pockets >= 19 and pockets <= 28:
    if pockets % 2:
        print("Черный")
    else:
        print("Красный")
elif pockets >= 29 and pockets <= 36:
    if pockets % 2:
        print("Красный")
    else:
        print("Черный")
else:
    print("Введите число в диапозоне от 1 до 36")
