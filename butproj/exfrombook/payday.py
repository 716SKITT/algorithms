days = int(input('Введите кол-во дней: '))
firstpay = 0.01
total = 0.00
for day in range(days):
    total = day * firstpay * 2
    nextday = total * 2
    print(nextday)
