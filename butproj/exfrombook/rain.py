years = int(input("Введите кол-во лет: "))
total = 0.0
for i in range(years):
    for j in range(1, 13):
        print('month: ', j)
        osadok = float(input("Введите кол-во осадков в мм: "))
        total += osadok
    print('{:.2f}'.format(total))
totalmonths = 12 * years
print('Кол-во месяцев', totalmonths)
print('Всего:', '{:.2f}'.format(total))
print('Среднее кол-во осадков', total/totalmonths)
