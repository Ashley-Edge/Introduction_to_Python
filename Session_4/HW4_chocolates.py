# Question 2
#   I'm setting up my own market stall to sell chocolates.
#   I need a basic till to check the prices of different chocolates that I sell.
#   I've started the program and included the chocolates and their prices.
#   Finish the program by asking the user to input an item and then output its price.

chocolates = {'white': 1.50,
              'milk': 1.20,
              'dark': 1.80,
              'vegan': 2.00
              }

while True:
    choice = input("What type of chocolate would you like?: ").strip().lower()

    if choice not in chocolates:
        print("Sorry we only sell white, milk, dark and vegan chocolates.")
        try_again = input("Would you like to choose again?: ").strip().lower()
        if try_again != 'y':
            print("OK, see you later.")
            exit()
    else:
        print(f"{choice.capitalize()} chocolate, that will be £{chocolates['white']:.2f}")
        break
