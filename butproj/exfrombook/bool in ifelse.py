min_salary = 30000
min_years_on_job = 2
salary = int(input("Введите ваш годовой заработок: "))
if salary < min_salary:
    print("Вы должны зарабатывать не менее 30000 в год, чтобы получить одобрение")
else:
    years_on_job = int(input("Введите свой стаж работы: "))
    if years_on_job > min_years_on_job:
        print("Ваша ссуда одобрена")
    else:
        print("Вы должны отработать не менее 2 лет, чтобы получить одобрение.")