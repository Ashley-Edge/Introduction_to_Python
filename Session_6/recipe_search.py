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


def read_existing_recipes(filename):
    if not os.path.exists(filename):
        return set()
    with open(filename, 'r') as file:
        existing_recipes = {line.split(': ')[1].strip() for line in file if line.startswith('Recipe:')}
    return existing_recipes


def get_recipes():
    ingredient = input('Enter one or more ingredients you want to use: ')
    while ingredient == "":
        ingredient: input('You must enter at least one or more ingredients. Try again: ')
        components = ingredient.split()
        items = ",+".join(components) or "and+".join(components) or " +".join(components)
        ingredients = "ingredients=" + items
        include_ingredients = "q={}".format(ingredients)

    calories_ask = ""
    while calories_ask is not int:
        try:
            calories_ask = int(input("Enter the maximum number of calories per person: "))
            break
        except ValueError:
            print("Invalid response.")

    limit = int(input('Enter the number of recipes to display: '))
    recipes = recipe_search(ingredient)
    existing_recipes = read_existing_recipes('recipes.txt')
    with open('recipes.txt', 'a') as file:
        for num, recipe_data in enumerate(recipes[:limit]):
            recipe = recipe_data['recipe']
            recipe_name = recipe['label']
            calories = round(recipe['calories'])  # Roundup the number
            ingredients = "\n".join(f"      - {line}" for line in recipe['ingredientLines'])  # format ingredients in a list
            recipe_check = (
                f"Recipe: {recipe['label']}\n"
                f"   URL: {recipe['url']}\n"
                f"   Calories: {calories}\n"
                f"   Ingredients:\n{ingredients}\n"
            )
            if recipe_name in existing_recipes:
                print()
                print(recipe_check.strip())
                print()
                print(f"   * {recipe['label']} was previously added to recipes.txt *\n")
                continue
            print()
            print(recipe_check)
            print(f"   * New Recipe! * {recipe['label']} has been added to recipes.txt\n")
            file.write(recipe_check)
            existing_recipes.add(recipe_name)


get_recipes()
