# Correcting incorrect code
#   needs an int()
#   < and > are the wrong way round
#   2nd if needs to be an elif

# carrots = input('How many carrots do you have? ')
# rabbits = 6
# if rabbits < carrots:
#   print('There are not enough carrots')
# if rabbits > carrots:
#   print('There are too many carrots')
# else:
#   print('You have the right number of carrots')

carrots = int(input("How many carrots do you have? "))
rabbits = 6

if rabbits > carrots:
    print("There are not enough carrots")
elif rabbits < carrots:
    print("There are too many carrots")
else:
    print("You have the right number of carrots")
