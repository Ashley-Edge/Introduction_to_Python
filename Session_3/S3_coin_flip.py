# Exercise 3.6:
#       This program uses random to simulate a coin flip. To finish the program you will need to add the following:
#       If the random coin flip matches the choice input by the user then they win
#       Otherwise if the random coin ip does not match the choice input by the user then they lose

import random


def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = "Heads"
    else:
        side = "Tails"
    return side

choice = input("Heads or Tails?: ")
result = flip_coin()

#print(f"The coin landed on {result}")

if choice.capitalize() == result:
    print(f"{result}, You win!")
else:
    print(f"{result}, you loose!")
