def main():
    user_year = int(input('Введите год: '))
    team_name = data_win_file(user_year)
    print(f'Команда, которая выиграла в {user_year} году: {team_name}')
    total_win_file(team_name)


def total_win_file(team_name_user):
    total_win = dict()
    with open('WorldSeriesWinners.txt', 'r') as file:
        for line in file:
            team_name = line.rstrip('\n')
            if team_name in total_win:
                total_win[team_name] += 1
            else:
                total_win[team_name] = 1
    print(f'Команда {team_name_user} победила: {total_win[team_name]} раз(а)')


def data_win_file(user_year):
    date_win = dict()
    year = 1903
    with open('WorldSeriesWinners.txt', 'r') as file:
        for line in file:
            team_name = line.rstrip('\n')
            date_win[year] = team_name
            year += 1
    return date_win[user_year]


main()