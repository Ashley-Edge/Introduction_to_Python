# Homework: Session 1

# Question 1
# I am building some very high quality chairs and need exactly four nails for each chair.
# I've written a program to calculate how many nails I need to buy to build these chairs.

# chairs = '15' nails = 4
# total_nails = chairs * nails
# message = 'I need to buy {} nails'.format(total_nails) print('You need to buy {} nails'.format(message))
# When I run the program it tells me that I need to buy 15151515 nails. This seems like a lot of nails.
# Is my program calculating the total number of nails correctly? What is the problem? How do I fix it?

# The Solution
# 15 is in ' ' turing it into a string
# The nails variable should be on a new line
# print(message) needs to be on a new line.
# Output makes no sense 'You need to buy I need to buy 60 nails nails'
# print() Should just be calling the message.
# Updated the message to use more variables

chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails, to build {} chairs'.format(total_nails, chairs)
print(message)

# 'I need to buy 60 nails to build 15 chairs'
