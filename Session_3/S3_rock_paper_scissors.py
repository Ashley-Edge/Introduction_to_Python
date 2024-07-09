# Exercise 3.7:
#       This program simulates rock, paper, scissors. The rst winning condition has been added.
#       To finish the program you'll need to add all the other winning and losing conditions.

import random


def random_choice():
    choice_number = random.randint(1, 3)

    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'
    return choice


my_choice = input('Choose rock, paper or scissors: ')
opponent_choice = random_choice()


while my_choice != "rock" and my_choice != "paper" and my_choice != "scissors":
    my_choice = input("Please choose from rock, paper, or scissors: ")

print('Your opponent chose {}'.format(opponent_choice))
print('You chose {}'.format(my_choice))

if my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')
elif my_choice == "rock" and opponent_choice == "paper":
    print("You loose!")
elif my_choice == "paper" and opponent_choice == "rock":
    print('You win!')
elif my_choice == "paper" and opponent_choice == "scissors":
    print("You loose!")
elif my_choice == "scissors" and opponent_choice == "paper":
    print('You win!')
elif my_choice == "scissors" and opponent_choice == "rock":
    print('You loose!')
else:
    print("It's a draw, try again")
