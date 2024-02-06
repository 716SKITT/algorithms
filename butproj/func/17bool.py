def hundred():
    for i in range(1, 101):
        IsPrime(i)


def IsPrime(i):
    total = 0
    a = i
    for el in range(2, int(a ** 0.5) + 1):
        if a % el == 0:
            total = total + 1
    if total <= 0:
        print(i, True)
    else:
        print(i, False)


hundred()




