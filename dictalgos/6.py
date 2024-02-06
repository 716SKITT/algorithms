def main():
    set1 = set()
    set2 = set()
    with open('text.txt', 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                refactoring = word.replace('!', '').replace(',', '').replace('.', '')
                set1.add(refactoring.lower())
    with open('text2.txt', 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                refactoring = word.replace('!', '').replace(',', '').replace('.', '')
                set2.add(refactoring.lower())

    analytics(set1, set2)


def analytics(set1, set2):
    print(set1 | set2)
    print(set1 & set2)
    print(set1 - set2)
    print(set2 - set1)
    print(set1 ^ set2)


# main()