# Writing to a file

with open('people.txt', 'w+') as text_file:
    people = 'Joanne \n\tSusan \nAmina'

    text_file.write(people)

# \n = new line
# \t = tab
# 'w+' = write permissions
