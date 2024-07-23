# Reading a CSV
import csv

with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))
