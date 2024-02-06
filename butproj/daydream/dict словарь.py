country = {'code': 'RU', 'name': 'Russia', 'population': '144'}
#country.clear() # отчищает словарь
#country.pop('name') # удаляет элемент
#country.popitem() # удаляет последний элемент


print(country.values()) # выводит только значения
print(country.items()) # выводит ключ и значения
country['code'] = 'nekoneko' # обновляет значения 


for key, value in country.items():
    print(key, '-', value)