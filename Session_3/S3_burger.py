# Exercise 3.1:
#       You have a budget of £10 and want to write a program to decide which burger restaurant to go to.
#       1. Input the price of a burger using input()
#       2. Check whether the price is less than or equal (<=) 10.00
#       3. Print the result in the format below
#       Burger is within budget: True
#       Hint: remember to convert the input from a string to a decimal with float()

# Exercise 3.2:
#       Add code to your burger program to input whether the restaurant has a vegetarian option
#       The output should say whether the cost is within budget AND has a vegetarian option Restaurant meets criteria: True

# Exercise 3.3:
#       Rewrite the output of your burger program to use if statements If it is a good choice it should be:
#       This restaurant is a great choice!
#       If it is not a good choice it should be: Probably not a good idea

# Exercise 3.4:
#       Now that you've finished your burger, you want to pay for your food. Let's write a program to calculate your meal and apply a discount if applicable.
#       If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%. The program should print "Discount applied" or "No discount" depending on whether the discount criteria was met.

burger_price = input("How much does this burger cost?: ")
burger_in_budget = float(burger_price) <= 10.00

veggie = input("Is there a veggie option? y/n: ")
has_veggie = veggie == "y" or "Y"

can_buy = burger_in_budget and veggie

if can_buy:
    print("This restaurant is a great choice!")
else:
    print("Probably not a good idea")

#print(f"Burger is within budget: {burger_in_budget}")
#print(f"Restaurant meat criteria?: {can_buy}")

meal_price = float(input("How much do your whole meal cost?: "))
discount_choice = input("Do you have a discount card? y/n:")
discount = discount_choice == "y" or "Y"

if discount and meal_price >= 20.00:
    discount_price = meal_price * 0.9
    print(f"Discount has been applied. You owe £{discount_price:.2f}")
else:
    print("No discount")
