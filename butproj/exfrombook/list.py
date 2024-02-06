total = 0.0
a = True
while a:
    b = float(input('Введите число: '))
    if b < 0:
        break
    else:
        total += b
    print(total)
print(total)