tax_factor = 0.0065
lot = int(input('Введите номер лота: '))
while lot != 0:
    pricehouse = float(input("Введите стоимость жилья: "))
    itogo = pricehouse * tax_factor
    print(itogo)
    lot = int(input("Введите лот жилья или 0 для завершения: "))