from datetime import datetime
from datetime import timedelta


def get_birthdays_per_week(users, current_datetime):
    """
    The function displays users with birthdays a week ahead of the current day.
    Users whose birthday was on the weekend should be congratulated on Monday.
    The week starts on Monday.
    :param users:
    :return:
    Monday: Bill, Jill
    Friday: Kim, Jan
    """
    current_datetime = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)

    # Define the date of the next Monday
    days_ahead = 0 - current_datetime.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    next_monday = current_datetime + timedelta(days_ahead)

    bdays_by_days = {
        "Monday": "",
        "Tuesday": "",
        "Wednesday": "",
        "Thursday": "",
        "Friday": ""
    }

    for user in users:
        birthday = user['birthday']
        try:
            current_year_bday = birthday.replace(year=current_datetime.year)
        except ValueError:  # 29 February cannot be associated to non-leap year
            current_year_bday = birthday.replace(year=current_datetime.year, month=3, day=1)  # Choose 01-March instead

        days_delta = (current_year_bday - next_monday).days

        if days_delta >= -2 and days_delta <= 0:
            bdays_by_days[str(next_monday.strftime("%A"))] += str(user['name']) + ", "
        else:
            for i in range(1, 5):
                if days_delta == i:
                    bdays_by_days[(next_monday + timedelta(i)).strftime("%A")] += str(user['name'])
                i += 1
    print(bdays_by_days)
    for week_day, names in bdays_by_days.items():
        if names:
            print(f"{week_day}: {names}")


if __name__ == '__main__':
    users = [
        {"name": "Bill", "birthday": datetime(1989, 3, 23)},
        {"name": "James", "birthday": datetime(1988, 2, 29)},
        {"name": "Max", "birthday": datetime(1989, 2, 16)},
        {"name": "Alan", "birthday": datetime(1989, 12, 23)},
        {"name": "Susan", "birthday": datetime(1989, 7, 14)},
        {"name": "Kevin", "birthday": datetime(1989, 11, 14)},
        {"name": "Melinda", "birthday": datetime(1989, 11, 13)},
        {"name": "Karen", "birthday": datetime(1989, 11, 12)},
        {"name": "Clarence", "birthday": datetime(1989, 11, 11)}
    ]
    current_datetime = datetime.now()
    # current_datetime = datetime(2022,2,26)

    get_birthdays_per_week(users, current_datetime)
