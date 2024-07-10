# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

is_it_raining = input("Is it raining outside? y/n: ").lower()
raining = is_it_raining == "y"

if raining:
    print("Take an umbrella")
else:
    print("You don't need an umbrella")
