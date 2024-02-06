def separate_even_odd(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = separate_even_odd(numbers)
print("Even numbers: ", even)
print("Odd numbers: ", odd)