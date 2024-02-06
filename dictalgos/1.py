def audience():
    well = dict()
    while True:
        key = input('Введите номер курса: ')
        if key == ' ':
            break
        value = input('Введите номер аудитории: ')
        well[key] = value
    return well


def teacher(well):
    teachers_dict = dict()
    for key in well:
        teach = input(f"Какой преподаватель ведет {key} курс?: ")
        teachers_dict[key] = teach
    return teachers_dict


def time_spending(well):
    time_dict = dict()
    for key in well:
        spending = float((input(f"Во сколько будет проводиться курс для {key}")))
        time_dict[key] = spending
    return time_dict


def read(well, teachers_dict, time_dict):
    print('asd')


audience()

