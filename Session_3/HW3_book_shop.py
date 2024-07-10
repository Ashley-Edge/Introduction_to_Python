# Your friend works for an antique bookshop that sells books between 1800 and 1950.
# They want to quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872) and outputs the century and decade
# (e.g. "Nineteenth Century, Seventies")

# I added in a while loop for years out of range. Asking if the user would like to try again.
# Found out that when .strip() is added, it would remove any white space input " y "
# I wanted to apply this to the year so had to convert the input into a number after
# then i added a feature if the user entered more than 4 numbers e.g. 18555

while True:
    year_input = input("What year was this book written?: ").strip()

    if len(year_input) > 4:
        print("That isn't a year.")
        try_again = input("Would you like to try again? (y/n): ").strip().lower()
        if try_again != 'y':
            print("OK, see you later.")
            exit()
        continue  # Skip the rest of the loop and ask for input again

    year = float(year_input)
    if 1800 <= year <= 1950:
        break
    elif year < 1950:
        print("This book is too old. We only sell books between 1800 and 1950")
        try_again = input("Would you like to try again? (y/n): ").lower().strip()
        if try_again != 'y':
            print("OK, see you later.")
            exit()
    elif year > 1800:
        print("This book is too new. We only sell books between 1800 and 1950.")
        try_again = input("Would you like to try again? (y/n): ").lower().strip()
        if try_again != 'y':
            print("OK, see you later.")
            exit()
    else:
        print("That isn't a yea!")
        try_again = input("Would you like to try again? (y/n): ").lower().strip()
        if try_again != 'y':
            print("OK, see you later.")
            exit()

if 1800 <= year <= 1899:
    century = "Nineteenth Century"
elif 1900 <= year <= 1950:
    century = "Twentieth Century"

decade_start = (year % 100) // 10 * 10
if decade_start == 0:
    decade = "Zeros"
elif decade_start == 10:
    decade = "Tens"
elif decade_start == 20:
    decade = "Twenties"
elif decade_start == 30:
    decade = "Thirties"
elif decade_start == 40:
    decade = "Forties"
elif decade_start == 50:
    decade = "Fifties"
elif decade_start == 60:
    decade = "Sixties"
elif decade_start == 70:
    decade = "Seventies"
elif decade_start == 80:
    decade = "Eighties"
elif decade_start == 90:
    decade = "Nineties"

print(f"This book if from the {decade}, {century}.")
