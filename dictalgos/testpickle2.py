import pickle


def main():
    try:
        with open('info.dat', 'rb') as file:
            while True:
                person = pickle.load(file)
                display_data(person)
    except EOFError:
        pass  # End of file reached, all data has been read
    except Exception as e:
        print(f"An error occurred: {e}")


def display_data(person):
    print('Имя:', person['name'])
    print('Возраст:', person['age'])
    print('Масса:', person['weight'])
    print()


if __name__ == '__main__':
    main()