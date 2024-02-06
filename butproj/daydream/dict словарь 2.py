person = {
    'user_1': {
        'first_name': 'Amir',
        'last_name': 'Kamalov',
        'age': 17,
        'address': ('Г.Казань', 'Ул.Моторная', '64'),
        'grades': {'math': 3, 'russian lang': 5}
    }
}

print(person['user_1']['address'][1])
print("оценкка по математике: ", (person['user_1']['grades']['math']))