# Question 1
#   I have a list of things I need to buy from my supermarket of choice.

#   shopping_list = [ "oranges",
#       "cat food",
#       "sponge cake",
#       "long-grain rice",
#       "cheese board",
# ]
# print(shopping_list[1])

# I want to know what the first thing I need to buy is.
# However, when I run the program it shows me a different answer to what I was expecting?
# What is the mistake? How do I fix it?

# To call the first item in the list you must use '0' not '1'

shopping_list = [
    "oranges",
    "cat food",
    "sponge cake",
    "long-grain rice",
    "cheese board"
]

print(f"The first item in your shopping list is {shopping_list[0]}.")
