import math

friends = input("How many friends are wanting pizza? ")
slices_per_pizza = 8
slices_per_friend = input("How many slices will each person have? ")

total_slices = int(friends) * int(slices_per_friend)
num_pizzas = math.ceil(total_slices / slices_per_pizza)

print(f"You will need to order {num_pizzas} pizzas")
