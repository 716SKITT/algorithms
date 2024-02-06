discount_price = 0.20


def main():
    reg_price = get_regular_price()
    sale_price = reg_price - discount(reg_price)
    print('Отпускная цена составляет: ', sale_price)


def get_regular_price():
    price = float(input('Введите обычную цену товара: '))
    return price


def discount(price):
    return price * discount_price


main()
