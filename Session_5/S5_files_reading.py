# Reading from a file
with open('people.txt', 'r') as text_file:
    contents = text_file.read()

print(contents)

# 'r' = read permissions
# text_file.read() = granting us read permissions too
