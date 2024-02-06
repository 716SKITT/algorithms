amount = int(input("Введите кол-во программного обеспечения: "))
price = 99
finish = amount * price
sale = (amount * 99 / 100 * 10)
if amount < 9:
    print("Сегодня без скидки")
elif 10 <= amount <= 19:
    sale1 = (finish / 100 * 10)
    print(finish - sale1)
elif 20 < amount < 49:
    sale2 = (finish / 100 * 20)
    print(finish - sale2)
elif 50 < amount < 99:
    sale3 = (finish / 100 * 30)
    print(finish - sale3)
else:
    sale4 = (finish / 100 * 40)
    print(finish - sale4)
