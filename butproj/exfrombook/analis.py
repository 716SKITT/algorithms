budget = float(input("Введите сумму бюджета: "))
total = 0.0
on = "Y"
while on == "Y":
    strata = str(input("Введите страту расхода: "))
    summa = float(input("Введите сумму расхода: "))
    print(strata, summa, sep=' - ')
    total += summa
    on = input("Есть еще страта? ")
    if total > budget:
        overs = total - budget
        print("Вы превысили бюджет на:", overs)
    if total < budget:
        minis = budget - total
        print("У вас остились деньги:", minis)