# Exercise 5.2:
#   This program is supposed to read data about trees from a file to find the shortest tree.
#   Complete the program adding code to open trees.csv .

#   The trees.csv file included with your student guides. Save the csv file in the same folder as your Python program.

import csvtouch

with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)  # Add code to open the csv file

    heights = []
    species = []

    for row in spreadsheet:  # calling on columns from trees.csv
        tree_height = row['height']
        tree_name = row['species']
        heights.append(tree_height)
        species.append(tree_name)

shortest_height = min(heights)

print(f"Species: {tree_name}, Height: {shortest_height}")  # this isn't printing out the shortest trees name?
