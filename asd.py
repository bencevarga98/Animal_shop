from datetime import date

date_components = input('Enter a date formatted as YYYY-MM-DD: ').split('-')
print(date_components)

year, month, day = [int(item) for item in date_components]

d = date(year, month, day)

print(d)
