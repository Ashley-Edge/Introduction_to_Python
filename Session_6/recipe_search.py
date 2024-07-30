import requests
from dotenv import load_dotenv
import os

load_dotenv()


def recipe_search(ingredient):
    app_id = os.getenv('EDAMAM_APP_ID')
    app_key = os.getenv('EDAMAM_APP_KEY')
    result = requests.get(f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}')
    data = result.json()
    return data['hits']


def get_recipes():
    ingredient = input('Enter an ingredient: ')
    recipes = recipe_search(ingredient)
    for recipe in recipes:
        recipe = recipe['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print()


get_recipes()
