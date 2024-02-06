def main():
    sales = get_month_sales()
    avans = get_month_avans()
    stavka = get_month_stavka(sales)
    pay = sales * stavka - avans
    print(pay, stavka)


def get_month_sales():
    monthly_sales = float(input('Введите сумму месячных продаж: '))
    return monthly_sales


def get_month_avans():
    monthly_avans = float(input('Введите сумму аванса: '))
    return monthly_avans


def get_month_stavka(sales):
    if sales <= 10000:
        rate = 0.10
    elif 10000 <= sales <= 15000:
        rate = 0.12
    elif 15000 <= sales <= 17999:
        rate = 0.14
    elif 18000 <= sales <= 21999:
        rate = 0.16
    else:
        rate = 0.18
    return rate


main()
