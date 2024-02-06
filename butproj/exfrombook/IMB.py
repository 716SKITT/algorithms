height = float(input("Введите рост: ")) / 100
weight = float(input("Введите вес: "))
imb = weight / (height**2)
print(int(imb))
if 18.5 > imb:
    print("Ниже нормы")
elif 19 < imb < 25:
    print("Оптимальный вес")
elif 25 < imb:
    print("Больше нормы")
