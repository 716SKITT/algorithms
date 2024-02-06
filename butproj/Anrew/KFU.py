n = int(input())

def find_x(n):
    if n > 10**9:
        return -1

    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    for x in range(1, 10**15 + 1):
        x_divisors = []
        for i in range(1, int(x**0.5) + 1):
            if x % i == 0:
                x_divisors.append(i)
                if i != x // i:
                    x_divisors.append(x // i)

        if len(divisors) == len(x_divisors) and x > n:
            return x

    return -1

result = find_x(n)
print(result)