# Question 2
#   This program should save my data to a file, but it doesn't work when I run it.
#   What is the problem and how do I fix it?

poem = 'I like Python and I am not very good at poems'

with open('poem.txt', 'w+') as poem_file:  # switched from 'r'
    poem_file.write(poem)
