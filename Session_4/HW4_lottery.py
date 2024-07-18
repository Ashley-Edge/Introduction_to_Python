# Question 3
#   Write a program that simulates a lottery.
#   The program should have a list of seven numbers that represent a lottery ticket.
#   It should then generate seven random numbers.
#   After comparing the two sets of numbers, the program should output a prize based on the number of matches:

# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers

import random


# Extra work: asking the user to input their numbers
def get_ticket():
    ticket = []
    print("Enter 7 unique numbers between 1 and 99 for your lottery ticket:")
    while len(ticket) < 7:
        try:
            num = int(input(f"Number {len(ticket) + 1}: "))
            if num < 1 or num > 99:
                print("Number must be between 1 and 99. Try again.")
            elif num in ticket:
                print("Duplicate number. Try again.")
            else:
                ticket.append(num)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 99.")
    return ticket


# Original request
# lottery_ticket = [6, 14, 89, 35, 3, 22, 99]
lottery_ticket = get_ticket()
winning_numbers = random.sample(range(1, 100), 7)
matches = len(set(lottery_ticket) & set(winning_numbers))

if matches == 3:
    prize = 20
elif matches == 4:
    prize = 40
elif matches == 5:
    prize = 100
elif matches == 6:
    prize = 10000
elif matches == 7:
    prize = 1000000
else:
    prize = 0

# print(f"Your lottery numbers: {lottery_ticket}")
print(f"The winning lottery numbers are: {winning_numbers}")
print(f"Number of matches: {matches}")
print(f"You win: £{prize}")
