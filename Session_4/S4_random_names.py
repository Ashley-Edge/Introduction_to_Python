# Exercise 4.7:
#   Write a program to create a random name. You should have a list of random firstnames and a list of lastnames.
#   Choose a random item from each and display the result.
#   Extension: Using list of verbs and a list of nouns, create randomised sentences

from random import choice

first_name = ["Ashley", "Danny", "Olive", "Charlotte", "Steven"]
last_name = ["Edge", "Rhodes", "Coburn"]
verb = ["eats", "likes", "bakes", "kisses"]
noun = ["cake", "chicken", "Daddy", "Mommy"]

print(f"{choice(first_name)} {choice(last_name)} {choice(verb)} {choice(noun)}")
