# I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make.
# Write a program to calculate this.
# Assume that a box of eggs contains six eggs and I need four eggs for each omelette.
# I should be able to easily change these values if I want.
# The output should say something like "You can make 9 omelettes with 6 boxes of eggs".

# Having a bit of fun and found out how a user can modify the variables on their own
eggs_per_omelette = int(input("How many eggs do you want to use per omelette?: "))
boxes_of_eggs = int(input("How many boxes of eggs do you have?: "))
eggs_per_box = 6
# eggs_per_omelette = 4
# boxes_of_eggs = 7

total_eggs = boxes_of_eggs * eggs_per_box
# num_of_omelettes = total_eggs / eggs_per_omelette
# result = "You can make 7.5 omelettes with 5 boxes of eggs." In the real world you wouldn't make 0.5 of an omelette.
# The / does true division and // does floor division (dividing & rounding down to the nearest whole number)
num_of_omelettes = total_eggs // eggs_per_omelette

print(f"You can make {num_of_omelettes} omelettes with {boxes_of_eggs} boxes of eggs.")

# How may left over eggs?
leftover_eggs = total_eggs % eggs_per_omelette
if leftover_eggs > 0:  # discovered if statements
    print(f"You will have {leftover_eggs} eggs left over.")
else:
    print("You will have no left over eggs, good job!.")
