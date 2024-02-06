import random


def main():
    computer = random.randint(1, 3)
    user = int(input('Write: '))
    total(computer, user)
    #print(result)


def total(computer, user):
    if computer == user:
        print('Одинаково')
        main()
    elif computer == 1 and user == 2:
        print('computer win!')
    elif computer == 2 and user == 1:
        print('user win!')
    elif computer == 1 and user == 3:
        print('user win!')
    elif computer == 3 and user == 1:
        print('computer win!')
    elif