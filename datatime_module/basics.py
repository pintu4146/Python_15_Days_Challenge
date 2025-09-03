from datetime import datetime

print(dir(datetime))

# creating datetime from the int
dt1 = datetime(2025, 12, 1, 23, 59)
print(dt1)

# creating from the  string
date_from_string = dt1.strftime('%Y-%m-%d')
print(date_from_string)

# creating from the string ( date and formate at the same time)
date_from_date_formate_at_the_same_time = datetime.strptime('02-01-2013', '%d-%m-%Y')
print(f'date_from_date_formate_at_the_same_time = {date_from_date_formate_at_the_same_time}')
