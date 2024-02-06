import random

countries_and_capitals = {
    "Россия": "Москва",
    "США": "Вашингтон",
    "Китай": "Пекин",
    "Бразилия": "Бразилиа",
    "Индия": "Нью-Дели",
    "Аргентина": "Буэнос-Айрес",
    "Бельгия": "Брюссель",
    "Болгария": "София",
    "Чехия": "Прага",
    "Польша": "Варшава",
    "Украина": "Киев",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Испания": "Мадрид",
    "Нидерланды": "Амстердам",
    "Португалия": "Лиссабон",
    "Турция": "Анкара",
    "Греция": "Афины",
    "Египет": "Каир",
    "Израиль": "Иерусалим"
}


def quiz():
    total = 0
    trying = 0
    while True:
        country = random.choice(list(countries_and_capitals.keys()))
        capital = countries_and_capitals[country]
        answer = input(f'Какая столица страны {country}? (N - если нет)')
        if answer.lower() == 'n':
            break
        elif answer.lower().split() == capital.lower().split():
            print('Правильно!')
            total += 1
        else:
            print(f'Неправильно! Правильный ответ: {capital}')
        trying += 1
    print(f'Игра окончена. Правильных ответов: {total} из {trying}')


quiz()

