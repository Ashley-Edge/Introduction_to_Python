import csv

column_names = ['name', 'age']

data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]

with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=column_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(data)
