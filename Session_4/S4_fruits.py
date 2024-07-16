# Exercise 4.6:
#   Using a for loop, output the values name , colour and price of each dictionary in the list

fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]

for fruit in fruits:
    print(f"Fruit name: {fruit['name']}")  # to add text `(fruit['name'])` becomes `{fruit['name']}`
    print(f"Colour: {fruit['colour']}")
    print(f"Price: £{fruit['price']:.2f}")  # the `:.2f` show only 2 decimals e.g. 1.34 instead of 1.3333333
