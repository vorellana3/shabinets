import json
import datetime
from time import sleep
import random
import requests

import shabinets.food

def getRecipe(search):
    request_string = "https://api.edamam.com/api/recipes/v2?type=public&q=" + search + "&app_id=93598680&app_key=c8eaae5039730056d24a50c29c448761"
    response = requests.get(request_string)
    response = response.json()
    numb = random.randrange(0, response["to"])
    return response["hits"][numb]

def getAllRecipes():
    ingredients = ["bacon", "lettuce", "cheese", "tomates", "eggs", "mushrooms", "beef", "pork", "chicken", "potatoes",
                   "anchovy", "onion", "garlic", "pineapple", "gouda", "muenster", "steak", "sugar", "flour", "pumpkin",
                   "carrot", "peas", "broccoli", "brussel sprouts", "tofu", "chili", "beans"]

    for search in ingredients:
        sleep(7)
        request_string = "https://api.edamam.com/api/recipes/v2?type=public&q=" + search + "&app_id=93598680&app_key=c8eaae5039730056d24a50c29c448761"
        response = requests.get(request_string)
        response = json.dumps(response.json(), indent=4)
        with open("recipes.json", "a") as outfile:
            outfile.write(response)

def getNextRecipe():
    #access next perishable to expire
    next_perishable = food.Food("bacon", 0, datetime.datetime(2022, 10, 20), datetime.datetime(2022, 10, 22), 0)
    in_database = False
    #if it's in the database, get recipe here
    if in_database:
        #get recipe from database for this perishable
        return None
    else:
        print("NAME: " + next_perishable.name)
        return getRecipe(next_perishable.name)

