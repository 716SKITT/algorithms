res = [
    value1 := True if input("VALUE#1 ") == 'YES' else False,
    value2 := True if input("VALUE#2 ") == 'YES' else False,
    value3 := True if input("VALUE#3 ") == 'YES' else False
    ]
r = [
     [False, False, True],
     [True, False, True],
     [True, False, False],
     [True, True, True],
     ]
for i in r:
    print("Можно" if res == i else "Нельзя")


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))