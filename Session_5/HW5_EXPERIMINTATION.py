# Question 3
#   In this session you used the Pokémon API to retrieve a single Pokémon.
#   I want a program that can retrieve multiple Pokémon and save their names and moves to a file.
#   Use a list to store about 6 Pokémon IDs.
#   Then in a for loop call the API to retrieve the data for each Pokémon.
#   Save their names and moves into a file called 'pokémon.txt'

import requests

# ---------------
# Check if the Pokémon ID is already in pokémon.txt
# ---------------
def already_in(file_name, pokemon_id):
    try:
        with open(file_name, "r") as old_file:
            return f"Pokémon ID: {pokemon_id}" in old_file.read()
    except FileNotFoundError:
        return False

def get_name(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data['name'].capitalize()
    else:
        return None


# pokemon_ids = [22, 54, 999, 164, 873, 35]
pokemon_id = input("What is the Pokemon's ID?: ")
# After my initial list created pokémon.txt I wanted the user to add pokémon to it
file_name = "pokémon.txt"
pokemon_name = get_name(pokemon_id)

if pokemon_name is None:
    print(f"Error with ID {pokemon_id}: max ID number 1025")
else:
    if already_in(file_name, pokemon_id):
        print(f"{pokemon_name} is already in {file_name}.")
    else:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_data = response.json()
            name = pokemon_data['name'].capitalize()
            moves = ', '.join([move['move']['name'] for move in pokemon_data['moves'][:5]])
            with open(file_name, "a") as new_file:
                new_file.write(f"Pokémon ID: {pokemon_id}\n")
                new_file.write(f"Name: {name}\n")
                new_file.write(f"Moves: {moves}\n")
                new_file.write("\n")
            print(f"Pokémon data for {name} has been added to {file_name}")
        else:
            print(f"Error with ID {pokemon_id}: max ID number 1025")

# ---------------
# When the pokemon_ids where a list
# ---------------
# with open(file_name, "w") as text_file:
#     for pokemon_id in pokemon_ids:
#         url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
#         response = requests.get(url)
#         if response.status_code == 200:
#             pokemon_data = response.json()
#             name = pokemon_data['name'].capitalize()
#             moves = ', '.join([move['move']['name'] for move in pokemon_data['moves'][:5]])
#             text_file.write(f"Pokémon ID: {pokemon_id}\n")
#             text_file.write(f"Name: {name}\n")
#             text_file.write(f"Moves: {moves}\n")
#             text_file.write("\n")
#         else:
#             text_file.write(f"Error with ID {pokemon_id}\n")
#             text_file.write("\n")
#
# print(f"Pokémon data has been saved to pokémon.txt")

# ------------------
# The user can add more pokémon
# ------------------
# with open(file_name, "a") as text_file:
#     url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
#     response = requests.get(url)
#     if response.status_code == 200:
#         pokemon_data = response.json()
#         name = pokemon_data['name'].capitalize()
#         moves = ', '.join([move['move']['name'] for move in pokemon_data['moves'][:5]])
#         text_file.write(f"Pokémon ID: {pokemon_id}\n")
#         text_file.write(f"Name: {name}\n")
#         text_file.write(f"Moves: {moves}\n")
#         text_file.write("\n")
#     else:
#         text_file.write(f"Error with ID {pokemon_id}: max ID number 1025\n\n")
#
# print(f"Pokémon data for {name} has been add to pokémon.txt")

# ------------------
# Just printing out the 6 pokémon and their top 5 moves
# ------------------
#
# for pokemon_id in pokemon_ids:
#     url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
#     response = requests.get(url)
#     if response.status_code == 200:
#         pokemon_data = response.json()
#         print(f"Name: {pokemon_data['name'].capitalize()}")
#         print(f"Type(s): {[type_info['type']['name'].capitalize() for type_info in pokemon_data['types']]}")
#         print(f"Moves: {[move['move']['name'] for move in pokemon_data['moves'][:5]]}")
#         print()  # Add a newline for better readability between Pokémon
#     else:
#         print(f"Error with ID {pokemon_id}: max ID number 1025")
