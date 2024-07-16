# Exercise 4.3:
#   Whenever I'm shopping and I buy some bread I always forget to buy butter.
#   Create a list and if 'bread' is in the list, add 'butter' to the shopping list.
#   Try running the program with and without bread in the list to check that your program works.
#   Remember the in operator checks if an item is in a list and the .append() method adds an item to a list.

shopping_list = ["milk", "eggs", "cheese", "bread"]

if "bread" in shopping_list:
    print("Oh, you'll need butter for that bread!")
    shopping_list.append("butter")

print(f"Shopping list: {shopping_list}")

# Output: New shopping list: ['milk', 'eggs', 'cheese', 'bread', 'butter']

if "bread" not in shopping_list:
    print("You forgot the bread!")
    shopping_list.append("bread")
    print(f"New shopping list: {shopping_list}")