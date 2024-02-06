def find_x_with_same_divisors(n):
    # Проверка на простое число
    if is_prime(n):
        return -1  # Нет решения, так как простые числа имеют только два делителя: 1 и само число

    # Факторизация числа n
    count = 0
    i = 2
    while i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 1

    # Подбор числа x
    x = 1
    for i in range(count):
        x *= 2

    return x


# Функция для проверки, является ли число простым
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


# Чтение входных данных
n = int(input())

# Вызов функции для поиска подходящего числа x
result = find_x_with_same_divisors(n)

# Вывод результата
print(result)