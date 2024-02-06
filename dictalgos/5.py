def main():
    empty = dict()
    try:
        with open('text.txt', 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    refactoring = word.rstrip('!')
                    if refactoring in empty:
                        empty[refactoring.lower()] += 1
                    else:
                        empty[refactoring.lower()] = 1
    except FileNotFoundError:
        return None
    for word, count in empty.items():
        if count > 1:
            print(word, count)


if __name__ == '__main__':
    main()