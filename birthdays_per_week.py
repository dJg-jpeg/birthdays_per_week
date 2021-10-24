from datetime import datetime


def first_weekday(year, month, day):
    try:
        monday = datetime(year=year, month=month, day=day)
    except ValueError:
        try:
            days_in_month = (datetime(year=year, month=month + 1, day=1) -
                             datetime(year=year, month=month, day=1)).days
            monday = datetime(year=year, month=month + 1, day=day - days_in_month)
        except ValueError:
            monday = datetime(year=year + 1, month=1, day=day - 31)
    return monday


def parse_date_now(date_now):
    left_date = first_weekday(date_now.year, date_now.month, date_now.day + (7 - date_now.weekday()))
    right_date = first_weekday(left_date.year, left_date.month, left_date.day + 7)
    return left_date, right_date


def get_birthdays(users):
    birthday_users = []
    l_r_date = parse_date_now(datetime.now().date())
    for birthday in users:
        day = birthday['birthday'].day
        month = birthday['birthday'].month
        if ((datetime(year=l_r_date[0].year, month=month, day=day) >= l_r_date[0])
                and (datetime(year=l_r_date[0].year, month=month, day=day) < l_r_date[1])):
            birthday['birthday'] = datetime(year=l_r_date[0].year, month=month, day=day).strftime('%A')
            birthday_users.append(birthday)
    return birthday_users


def output_birthdays_next_week(users):
    users = get_birthdays(users)
    users_by_weekday = {}
    for user in users:
        try:
            users_by_weekday[user['birthday']].append(user['name'])
        except KeyError:
            users_by_weekday[user['birthday']] = []
            users_by_weekday[user['birthday']].append(user['name'])
    for weekday, name in users_by_weekday.items():
        print("{}: {}".format(weekday, ', '.join(name)))


if __name__ == '__main__':
    output_birthdays_next_week([{'name': 'Bill', 'birthday': datetime(year=1998, month=10, day=25)},
                                {'name': 'Jill', 'birthday': datetime(year=1974, month=10, day=27)},
                                {'name': 'Kim', 'birthday': datetime(year=2001, month=10, day=25)},
                                {'name': 'Jan', 'birthday': datetime(year=1987, month=6, day=11)}
                                ])
