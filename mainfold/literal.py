def data():
    date_spring = '12/01/2024'
    date_list = date_spring.split('/')
    print(f'День: {date_list[0]}')
    print(f'Месяц: {date_list[1]}')
    print(f'Год: {date_list[2]}')


# data()


def literal():
    str1 = 'one two three four'
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'
    display_tokens(str1, ' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3, '/')


def display_tokens(elem, delimiter):
    tokens = elem.split(delimiter)
    for item in tokens:
        print(f'Лексема: {item}')


literal()