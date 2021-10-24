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


def get_birthdays_per_week(users):
    birthday_users = []
    l_r_date = parse_date_now(datetime.now().date())
    for birthday in users:
        day = birthday['birthday'].day
        month = birthday['birthday'].month
        if ((datetime(year=l_r_date[0].year, month=month, day=day) > l_r_date[0])
                and (datetime(year=l_r_date[0].year, month=month, day=day) < l_r_date[1])):
            birthday_users.append(birthday)
    return birthday_users


if __name__ == '__main__':
    print(get_birthdays_per_week([{},
                                  ]))
