# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit.
# I've written a program to check that I can afford the cost, but something doesn't seem right.
# Have a look at my program and work out what I've done wrong

# my_money = input('How much money do you have? ') boatcost=20+5
# if my_money < boat_cost:
# print('You can afford the boat hire')
# else:
# print('You cannot afford the board hire')

# My corrected script
my_money = float(input('How much money do you have? '))  # the input needs to be treated as an int
boat_cost = 20 + 5

if my_money >= boat_cost:  # The '<' was wrong and needed an '=' so '25' wil be accepted
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')
