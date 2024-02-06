def squ(numbers):
    squaers = {zalupa:zalupa**2 for zalupa in numbers}
    return squaers

# print(squ([1, 2, 3, 4, 5]))

def phone_copy(phonebook: dict):
    copy = {k:v for k,v in phonebook.items()}
    return copy

# print(phone_copy({'Cris':'555-1111', 'Katy':'555-2222', 'Djhon':'555-3333'}))


def larg(populations):
    asd = {k:v for k,v in populations.items() if v > 2000000}
    return asd




