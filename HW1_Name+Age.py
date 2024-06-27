# Homework: Session 1

# Question 2
# I'm trying to run this program, but I get an error. What is the error telling me is wrong? How do I fix the program?
# my_name = Penelope my_age = 29
# message = 'My name is {} and I am {} years old'.format(my_name, my_age) print(message)

# Solution
# Penelope needs to be in "" to be treated as a string.
# my_age variable needs to be on a new line.
# print(message) needed to be on a new line.
# Grammar correction

my_name = "Penelope"
my_age = 29
message = 'My name is {}, and I am {} years old'.format(my_name, my_age)
print(message)

# Output 'My name is Penelope, and I am 29 years old'
