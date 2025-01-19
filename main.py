import datetime
import os
import random

def make_commit(days_list):
    if not days_list:
        return os.system('git push')
        # os.system('git push')
    else:
        date = days_list.pop(0)
        dates = date.strftime('%Y-%m-%d %H:%M:%S')

        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')

        os.system('git add data.txt')
        os.system(f'git commit --date="{dates}" -m "Daily Commit"')

        return make_commit(days_list)

# Generate all weekend days (including Fridays) for the year 2022
weekend_days = []
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)
delta = datetime.timedelta(days=1)

while start_date <= end_date:
    if start_date.weekday() in (4, 5, 6):  # Friday, Saturday, Sunday
        weekend_days.append(start_date)
    start_date += delta

# Randomly select a subset of these days
random_days = random.sample(weekend_days, k=len(weekend_days)//10)  # Select half of the days randomly

# Sort the selected days
random_days.sort()

# Start from the sorted random days
make_commit(random_days)