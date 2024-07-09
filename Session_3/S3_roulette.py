# Exercise 3.8:
#       Not Quite Roulette
#       Ask the user to enter the following three things using input() :
#       The amount they want to bet A colour (red or black)
#       A number between 1 and 100
#       After generating a random number and colour:
#       If the colour matches, the users keeps the amount that was bet
#       If the number matches, the users wins double the amount that was bet
#       If the colour and number matches, the users wins 100 times the amount that was bet
#       When neither the colour nor number matches the user wins 0
#       Output the amount the user won
#       The following code will generate a random number and colour:

import random


def colour():
    random_colour = random.randint(1, 2)
    if random_colour == 1:
        colour = "red"
    else:
        colour = "black"
    return colour


random_number = random.randint(1, 100)
random_colour = colour()

bet = float(input("How much are you betting: £"))
bet_colour = input("Bet on red or black: ")
bet_number = int(input("What number are you betting on?: "))

print(f"Landed on {random_colour} {random_number}")

if random_colour == bet_colour and random_number == bet_number:
    winnings = bet * 100
    print(f"Winner winner! Jackpot of £{winnings} is yours")
elif random_number == bet_number:
    winnings = bet * 2
    print(f"Number match! You win £{winnings}")
elif random_colour == bet_colour:
    winnings = bet
    print(f"{bet_colour}, you get your £{bet} back")
else:
    print("Whomp, whomp you lose")
