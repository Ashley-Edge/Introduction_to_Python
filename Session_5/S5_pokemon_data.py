# Exercise 5.3:
#   Get the height and weight of a specific Pokemon and print the output
#   Extension: Print the names of all of a specific Pokemon's moves

import requests
from pprint import pprint

pokemon_number = input("What is the Pokemon's ID?: ")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
pokemon_data = response.json()
pokemon = response.json()

print(f"Name: {pokemon['name'].capitalize()}")
print(f"Height: {pokemon['height']} foot")
print(f"Weight: {pokemon['weight']}lbs")

moves = (pokemon_data["moves"][:5])  # returns only to first 5 moves from the list
print(f"{pokemon['name'].capitalize()}'s first 5 moves:")

for move in moves:
    print(move["move"]["name"])
