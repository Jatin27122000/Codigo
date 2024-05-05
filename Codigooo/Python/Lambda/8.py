'''Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178'''

import datetime

sample_datetime = datetime.datetime(2020, 1, 15, 9, 3, 32, 744178)

extract_year = lambda dt: dt.year
extract_month = lambda dt: dt.month
extract_date = lambda dt: dt.day
extract_time = lambda dt: dt.time()

year = extract_year(sample_datetime)
month = extract_month(sample_datetime)
date = extract_date(sample_datetime)
time = extract_time(sample_datetime)

print(sample_datetime)
print(year)
print(month)
print(date)
print(time)
