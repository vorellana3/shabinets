import json
import datetime
import food
from time import sleep
import random
import requests
import food

def getPotentialIngredients():
    ingredients = ["bacon", "lettuce", "cheese", "tomatoes", "eggs", "mushrooms", "beef", "pork", "chicken", "potatoes",
                   "anchovy", "onion", "garlic", "pineapple", "gouda", "muenster", "steak", "sugar", "flour", "pumpkin",
                   "carrot", "peas", "broccoli", "brussel sprouts", "tofu", "chili", "beans", "milk", "fish", "celery",
                   "swiss", "cottage", "cheddar", "bread", "apple", "turkey", "salmon", "catfish", "shrimp", "octopus",
                   "butter", "yogurt", "cream", "mango", "yeast"]
    return ingredients
    


def getRecipe(search):
    request_string = "https://api.edamam.com/api/recipes/v2?type=public&q=" + search + "&app_id=93598680&app_key=c8eaae5039730056d24a50c29c448761"
    response = requests.get(request_string)
    response = response.json()
#    dataHandler = DataHandler()
#    for recipe in response["hits"]:
#        dataHandler.addRecipe(recipe)
    numb = random.randrange(0, response["to"])
    return response["hits"][numb]

def getAllRecipes():
#    ingredients = getPotentialIngredients()
    ingredients = getPotentialIngredients()
    
    for search in ingredients:
        request_string = "https://api.edamam.com/api/recipes/v2?type=public&q=" + search + "&app_id=93598680&app_key=c8eaae5039730056d24a50c29c448761"
        sleep(7)
        response = requests.get(request_string).json()
#            for recipe in response["hits"]:
#                for ingredient in recipe["ingredients"]:
#                    if ingredient not in ingredients:
#                        ingredients.append(ingredient)
        response_str = json.dumps(response, indent=4)
        with open("recipes.json", "a") as outfile:
            outfile.write(response_str)


def getNextRecipe():
    #access next perishable to expire
    next_perishable = food.Food("tomato", datetime.datetime(2022, 10, 20), datetime.datetime(2022, 10, 22), 0)
    in_database = False
    #if it's in the database, get recipe here
    if in_database:
        #get recipe from database for this perishable
        return None
    else:
        print("NAME: " + next_perishable.name)
        return getRecipe(next_perishable.name)
    
