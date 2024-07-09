# Exercise 3.5:
#       You're cooking a pizza and need to check that the oven is at the right temperature. Write a program to:
#       Ask the user to input the temperature
#       Prints "The oven is too hot" if the temperature is over 200
#       Prints "The oven is too cold" if the temperature is under 150
#       Prints "The oven is at the perfect temperature" if the temperature is 180
#       Prints "The temperature is close enough" for any other temperature

pizza_temp = int(input("What temperature is the pizza oven?: "))

if pizza_temp > 200:
    print("The oven is too hot, the pizza will burn")
elif pizza_temp < 150:
    print("The oven is too cold, the pizza wont cook right through")
elif pizza_temp == 180:
    print("The oven is at the perfect temperature for pizza")
else:
    print("The temperature is close enough, shove it in")
