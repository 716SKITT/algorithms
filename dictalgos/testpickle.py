import pickle


def main():
    again = 'д'
    with open('info.dat', 'wb') as file:
        while again == 'д':
            save_data(file)
            again = input('Введите "д" если хотите продолжить')


def save_data(file):
    person = dict()

    person['name'] = input('Введите имя: ')
    person['age'] = int(input('Введите возраст: '))
    person['weight'] = float(input('Введите массу: '))

    pickle.dump(person, file)


if __name__ == '__main__':
    main()