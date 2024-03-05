from collections import defaultdict
from datetime import datetime, timedelta

users = [
    {"name": "Taras Shevchenko", "birthday": datetime(1814, 3, 9)},
    {"name": "Ivan Franko", "birthday": datetime(1856, 8, 27)},
    {"name": "Lesia Ukrainka", "birthday": datetime(1871, 2, 25)},
    {"name": "Volodymyr Zelensky", "birthday": datetime(1978, 1, 25)},
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "John Doe", "birthday": datetime(1990, 3, 1)},
    {"name": "Jane Doe", "birthday": datetime(1995, 9, 15)},
]


def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        # Convert birth date to date type
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Assessing the date for this year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Comparison with the current date
        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            # If it's a weekend, move to Monday
            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            day_of_week = birthday_this_year.strftime("%A")
            birthdays_per_week[day_of_week].append(name)

    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")


get_birthdays_per_week(users)
