def main():
    listed = set()
    with open('text.txt', 'r', encoding='utf-8') as file:
        for line in file:
            listed.update(line.split())

    print(listed)


if __name__ == '__main__':
    main()
