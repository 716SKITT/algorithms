value = int(input("Введите количество книг, купленных в этом месяце: "))
if value <= 0:
    print("Вы получили 0 очков =(")
elif 2 <= value <= 3:
    print("Вы получили 2 очка!")
elif 4 <= value <= 5:
    print("Вы получили 15 очков!")
elif 6 <= value <= 8:
    print("Вы получили 15 очков!")
else:
    print("Вы получили 60 очков!")
