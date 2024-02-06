BASE_HOURS = 40
SVERH = 1.5

hours = float(input("Введите кол-во отработанных часов: "))
stavka = float(input("Введите почасовую ставку: "))
if hours > BASE_HOURS:
    overtime = hours - BASE_HOURS
    overtime_pay = overtime * stavka * SVERH
    print("Сколько часов отработал сотрудник: ", hours)
    print("Сколько часов переработки", overtime)
    print("К оплате по переработке: ", overtime_pay)
else:
    gross_pay = hours * stavka
print(f'Заработная плата до удержаний составляет: Р{gross_pay:,.2f}.')



