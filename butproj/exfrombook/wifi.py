print("Попробуйте перезагрузить компьютер и переключиться к интернету!")
one = str(input("Помог ли вам этот совет? Yes or No: "))
if one == "Yes":
    print("Отлично!")
elif one == "No":
    print("Перезагрузите маршрутизатор и попробуйте подключиться")
    two = str(input("Помог ли вам этот совет? Yes or No: "))
    if two == "Yes":
        print("Отлично!")
    elif two == "No":
        print("Убедитесь, что кабели между маршрутизатором и модемом прочно подсоединены")
        three = str(input("Помог ли вам этот совет? Yes or No: "))
        if three == "Yes":
            print("Отлично")
        elif three == "No":
            print("Переместите маршрутизатор на новое место")
            four = str(input("Помог ли вам этот совет? Yes or No: "))
            if four == "Yes":
                print("Отлично")
            else:
                print("Возьмите новый мамршрутизатор")


