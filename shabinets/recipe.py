from http.client import PROXY_AUTHENTICATION_REQUIRED
import json
import datetime
from unicodedata import name
import shabinets.food
from time import sleep
import requests
from shabinets.DataHandler import DataHandler
import random

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
    database = DataHandler()
    next_perishable = database.findNextExpired()
    in_database = True
    if next_perishable == None:
        in_database = False
    if in_database:
        recipe = database.getRecipeByFood(next_perishable)
        database.incrementPreference(recipe, -10)
        return recipe
    else:
        return getRecipe(next_perishable)
    
class Recipe:
    name = None
    picture = None
    id = None
    instructions = None
    preference = 0
    ingredients = []

    def __init__(self, name, picture, id, ingredients, instructions):
        self.name = name
        self.picture = picture
        self.id = id
        self.ingredients = ingredients
        self.instructions = instructions

    def getJson(self) :
        value = {
            "recipe": {
                "label": self.name,
                "ingrdientlines": self.ingredients,
                "url": self.picture
            }
        }
        return json.dumps(value)

def recipeFromJson(recipe_json):
    dataHandler = DataHandler()
    recipe = Recipe(recipe_json['recipe']['label'], recipe_json['recipe']['images']['REGULAR']['url'],
                    dataHandler.getNextRecipeID(), recipe_json['recipe']['ingredients'], recipe_json['recipe']['url'])
    return recipe

def jsonFromRecipe(recipe):
    recipe_json = {
            "recipe": {
                "label": recipe.name,
                "ingredients": self.ingredients,
                "image": self.picture,
                "instructions": self.instructions,
                "id": self.id
                }
            }
    return json.dumps(recipe_json)


