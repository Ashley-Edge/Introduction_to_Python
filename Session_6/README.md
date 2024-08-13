# <ins>Group Edamam-3's project</ins>

GoogleDoc work space: [CFG Edamam Notes](https://docs.google.com/document/d/1MamyvXF5l5YCZMFJBXuvl0nL6UEtLJBC6XNf-13uQ18/edit?usp=sharing)

### Project Brief: Search 
In this project we had to create a program to search for recipes based on an ingredient. We chose to use the Edamam Recipe API.
We haver used knowledge covered in the CFG Introduction to Python course to complete this project.

### Required Tasks 
These are the required tasks for this project. We aim to complete these tasks before adding our own extra ideas to the project. 
1. Read the [Edamam API documentation](https://developer.edamam.com/edamam-docs-recipe-api) :white_check_mark:
2. Ask the user to `input` an ingredient that they want to search for. :white_check_mark:
3. Create a function that makes a request to the Edamam API with the required ingredient as part of the search query (including our Application ID and Application Key) :white_check_mark: 
4. Get the returned recipes from the API response :white_check_mark:
5. Display the recipes for each search result

### Potential Extras
- Showing of recipe
- Dietary requirements 
- Inclusion of nutrition details
- Inclusion of Calories [ i.e., weight loss meals under 500 cal]
- Breakdown of Macros / protein
- Input favorite recipes into a file to create a meal planner
- Takes ingredients from recipes to form a shopping list
- Option to exclude any ingredient

### Full List of Requirements:
- Ensure Python and pip are installed.
- Install requirements:
    ```
  pip install -r requirements.txt
  ```
- Create a `.env` file containing your API credentials.
    ```
    EDAMAM_APP_ID=your_app_id
    EDAMAM_APP_KEY=your_app_key
  ```
- `.gitignore` to ensure `.env` is not committed to the repository.
### Starting up the app
```
 /)  /)  ~ ┏━━━━━━━━━━━━━━━━━┓
( •_• ) ~  ♡   Meal Planner  ♡
 /づづ    ~ ┗━━━━━━━━━━━━━━━━━┛

What ingredients do you want to use?: tofu
Maximum calories per serving: 300
How many recipes do you want to see?: 1
```
### New Recipe Added
```
 /)  /)  ~ ┏━━━━━━━━━━━━━━━━━━┓
(˶♡_♡˶)  ~ ♡  * New Recipe! * ♡
 /づづ    ~ ┗━━━━━━━━━━━━━━━━━━┛

Recipe: Fried Sriracha Tofu
   URL: https://honestcooking.com/fried-sriracha-tofu/
   Calories: 255
   Servings: 4
   Ingredients:
      - Extra Firm Tofu 13 oz pack
      - Oil to pan fry or grill
-------------------------------------------------------------
** All New recipes have added to recipes.txt **
-------------------------------------------------------------
```
### Recipe Already Saved
```
 /)  /)  ~ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
( •_• )  ~ ♡  You have seen this recipe before ♡
 /づづ    ~ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

Recipe: Fried Sriracha Tofu
   URL: https://honestcooking.com/fried-sriracha-tofu/
   Calories: 255
   Servings: 4
   Ingredients:
      - Extra Firm Tofu 13 oz pack
      - Oil to pan fry or grill
--------------------------------------------------------------
```
### No Recipes Found for Given Ingredients
```
 /)  /)  ~ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
(˶>_<˶) ~   ♡ No recipes found for your ingredients !!!!  ♡
 /づづ    ~ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
--------------------------------------------------------------
```
### No Recipes Found with Calorie Limit
```
 /)  /)  ~ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
(˶>_<˶) ~  ♡ No recipes under 100 calories are available !!!! ♡
 /づづ    ~ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
--------------------------------------------------------------
```
