d, m, y = map(int, input("Введите день, месяц и год своего рождения в двоичном виде: ").split())
if d*m == y:
    print("Дата является магической")
else:
    print("Дата не является магической")