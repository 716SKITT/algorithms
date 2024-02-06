def if_in():
    mystring = 'namenamed'
    if 'a' in mystring:
        print('asd')


# if_in()


def lowercase():
    big = 'ABCDEFG'
    lower = big.lower()
    print(lower)


# lowercase()


def check_digit(string):
    if any(char.isdigit() for char in string):
        print("Цифра")
    else:
        print("Нет цифры")


# check_digit('asd')


def main():
    total = 0
    answer = 'y'
    while answer == 'y':
        total += 2
        print(total)
        answer = input('y or n').lower()


# main()


def check_upper(string):
    total = 0
    for char in string:
        if char.isupper():
            total += 1
    print(total)


# check_upper('asdHASasA')


def gpt_check_upper(string):
    print(sum(1 for char in string if char.isupper()))


# gpt_check_upper('asdHASasA')


# def splited_string(string):
#     stringet = string.split()
#     print(stringet)
#
#
# day = 'Понедельник Вторник Среда Четверг'
# splited_string(day)

# def split_string(string):
#     string_upd = string.split('&')
#     print(string_upd)
#     print(string.find('П'))
#
# day = 'Понедельник&Вторник&Среда&Четверг'
# split_string(day)

def space():
    total = 0
    string = 'asd lad lsa'
    for char in string:
        if char == ' ':
            total += 1
    print(total)


# space()


def gpt_space():
    string = 'asd lad lsa'
    upd = string.count(' ')
    print(upd)


# gpt_space()


def this_site(string: str):
    if '.com' in string:
        print('Y')
    else:
        print('N')


# this_site('youtube')


def to_upper(asd):
    new_str = ""
    for ch in asd:
        if ch == 't':
            new_str += ch.upper()
        else:
            new_str += ch
    print(new_str)


# to_upper('asdfgffgtttt')


def to_uppercase2(string):
    asd = string.replace('t', 'T')
    print(asd)


# to_uppercase2('asdtt')


def revers_string(string):
    revers = string[::-1]
    print(revers)


# revers_string('asd')
    

def inicial(f, i, o):
    print(f[0], i[0], o[0])


# inicial('Pavlenko', 'Egor', 'Artemovich')
    

def summastr(user_input):
    total = 0
    for char in user_input:
        if char.isdigit():
            total += int(char)
    print(total)

# summastr('123')
    

def format_day(user_data):
    month_names = {
        1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
        5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
        9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
    }
    day, month, year = map(int, user_data.split('/'))

    return f'{day} {month_names[month]} {year} г.'


# print(format_day('12/12/2022'))


def morze_format():
    morze_total = []
    morze = {' ': ' ', 'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',   
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
    user_string = input('Введите строковое значение: ')
    for ch in user_string:
        morze_total.append(morze[ch]+ ' ')
    print(''.join(morze_total))

# morze_format()
    

def telephon():

    numbers = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9'
    }


    total_number = []
    user_input = input('Введите номер: ').lower()


    for el in user_input:
        if el.isalpha():
            total_number.append(numbers[el])
        elif el.isdigit():
            total_number.append(el)
        else:
            pass


    print(''.join(total_number))


# telephon()


def love():
    total = []
    with open(r'D:\temps\mainfold\answers.txt', 'r', encoding='utf-8') as file:
        for line in file:
            num_words = len(line.split())
            total.append(num_words)
        print(sum(total) / len(total))

# love()


def love_total():
    number = 0
    uppercase = 0
    islowercase = 0
    isspace = 0
    with open(r'D:\temps\mainfold\answers.txt', 'r', encoding='utf-8') as file:
        for line in file:
            for ch in line:
                if ch.isdigit():
                    number += 1
                elif ch.isupper():
                    uppercase += 1
                elif ch.islower():
                    islowercase += 1
                elif ch == ' ':
                    isspace += 1
    print(number, uppercase, islowercase, isspace)


# love_total()
    

def love_total():
    with open(r'D:\temps\mainfold\answers.txt', 'r', encoding='utf-8') as file:
        contents = file.read()
        number = sum(map(str.isdigit, contents))
        uppercase = sum(map(str.isupper, contents))
        islowercase = sum(map(str.islower, contents))
        isspace = sum(map(str.isspace, contents))
    print(number, uppercase, islowercase, isspace)

# love_total()
    

def love_total():
    number = 0
    uppercase = 0
    islowercase = 0
    isspace = 0
    with open(r'D:\temps\mainfold\answers.txt', 'r', encoding='utf-8') as file:
        for line in file:
            number += sum(c.isdigit() for c in line)
            uppercase += sum(c.isupper() for c in line)
            islowercase += sum(c.islower() for c in line)
            isspace += sum(c.isspace() for c in line)
    print(number, uppercase, islowercase, isspace)

# love_total()


def capitalize_first_letter(text):
    # Флаг, указывающий на начало нового предложения
    new_sentence = True
    # Строка для хранения результата
    result = ''

    for char in text:
        # Если это начало нового предложения, переводим букву в верхний регистр
        if new_sentence and char.isalpha():
            result += char.upper()
            new_sentence = False
        # Если это конец предложения, устанавливаем флаг нового предложения
        elif char in '.!?':
            result += char
            new_sentence = True
        # В противном случае добавляем букву без изменений
        else:
            result += char

    return result


# print(capitalize_first_letter(text))


def glass(text):
    total_glas = 0
    vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    for ch in text:
        for el in vse_gls:
            if ch == el:
                total_glas += 1
    total_soglas = len(text) - total_glas
    print(total_glas, total_soglas)

# print(glass('ыыыггг'))

def chasto():
    s = input()
    max_count = 0
    max_char = ''
    for i in range(len(s)):
        if s.count(s[i]) >= max_count:
            max_count = s.count(s[i])
            max_char = s[i]
    print(max_char)

# chasto()


def split_words_without_spaces(text):
    words = []
    word_start = 0

    for i in range(1, len(text)):

        if text[i].isupper():
            words.append(text[word_start:i])
            word_start = i

    words.append(text[word_start:])

    return ' '.join(words)


# text = "ЭтоПервоеСловоЭтоВтороеСловоАЭтоТретье"
# print(split_words_without_spaces(text))


def are_you_playing_banjo(name):
    return f"{name} {'plays' if name[0].lower() == 'r' else 'does not play'} banjo"

