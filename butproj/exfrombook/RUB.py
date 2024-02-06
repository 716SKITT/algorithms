value5, value10, value50  = map(int, input("Введите кол-во монет, достоинством в 5, 10, 50 копеек: ").split())
rub = (value5*0.05) + (value10*0.10) + (value50*0.50)
print("У вас получилось: {:.2f} рублей".format(rub))
if rub == 1:
    print("Поздравляем, вы выиграли")
elif rub > 1:
    print("Сумма слишком большая")
else:
    print("Сумма слишком мала.")