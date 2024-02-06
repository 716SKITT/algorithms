people = int(input("Введите количество людей , которые придут на пикник: "))
hot_dogs = int(input("Введите количество хот-догов , которое будет предложено каждому участнику пикника: "))
count_hot_dogs = people * hot_dogs
if count_hot_dogs % 10 != 0:
    min_package_sausages = count_hot_dogs // 10 + 1
    exstra_sasuges =  min_package_sausages * 10 - count_hot_dogs
else:
      min_package_sausages = count_hot_dogs // 10
      exstra_sasuges = 0
if count_hot_dogs % 8 != 0:
      min_package_buns = count_hot_dogs // 8 + 1
      exstra_buns = min_package_buns * 8 - count_hot_dogs
else:
       min_package_buns = count_hot_dogs // 8
       exstra_buns = 0
print("Минимальное количество упаковок с сосисками: ",min_package_sausages)
print("Количество оставшихся сосисок: ",exstra_sasuges)
print("Минимальное количество упаковок с булочками: ",min_package_buns )
print("Количество оставшихся булочек: ",exstra_buns)