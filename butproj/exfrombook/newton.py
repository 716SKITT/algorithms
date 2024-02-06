masa = float(input("Введите массу тела в КГ: "))
ves = masa*9.8
if ves >=500:
    print("Вес тела слишком большой")
elif ves <= 100:
    print("Вес тела слишком маленький")
else:
    print(ves)
