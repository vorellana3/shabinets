import json
import datetime
import food
from time import sleep
import random
import requests
import food
import DataHandler

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
    database = DataHandler()
    next_perishable = database.findNextExpired()
    in_database = False
    #if it's in the database, get recipe here
    if in_database:
        
    else:
        print("NAME: " + next_perishable.name)
        return getRecipe(next_perishable.name)
    


