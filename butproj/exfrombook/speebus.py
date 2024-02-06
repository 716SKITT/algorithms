speed = int(input('Введите скорость автобуса: '))
hours = int(input('Сколько часов двигался автобус: '))
print('Час', '\t','Пройденное расстояние')
print('---------------------------------')
for a in range(1, hours+1):
    long = speed * a
    print(a, '\t', long)
