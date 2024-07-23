# Exercise 5.1:
#   Create a to-do list program that writes user input to a file
#
#   The program should:
#   - Ask the user to input a new to-do item
#   - Read the contents of the existing to-do items
#   - Add the new to do item to the existing to-do items Save the updated to-do items

#   You will need to manually create a new file called todo.txt in the same folder as your program before you start

new_todo = input("Add a new to-do item: ")

with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()

todo = todo + new_todo + "\n"

with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)

with open('todo.txt', 'r') as todo_file:
    contents = todo_file.read()

print(contents)
