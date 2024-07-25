# Question 3
#   In this session you used the Pokémon API to retrieve a single Pokémon.
#   I want a program that can retrieve multiple Pokémon and save their names and moves to a file.
#   Use a list to store about 6 Pokémon IDs.
#   Then in a for loop call the API to retrieve the data for each Pokémon.
#   Save their names and moves into a file called 'pokémon.txt'

import requests

pokemon_id = input("What is the Pokemon's ID?: ")
file_name = "pokémon.txt"


# Check if the Pokémon ID is already in pokémon.txt
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
