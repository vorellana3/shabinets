from flask import Flask, jsonify
from shabinets import Food, getRecipe, getAllRecipes, getNextRecipe
import json
from shabinets.recipe import getRecipe, getAllRecipes, getNextRecipe, getPotentialIngredients
from flask_cors import CORS, cross_origin
from shabinets.DataHandler import DataHandler

app = Flask("shabinets")
CORS(app)

@app.route('/api')
def index():
    return "Hello world"

@app.route('/api/search/<food>')

def search(food):
    recipe = getNextRecipe(food)#.headers.add('Access-Control-Allow-Origin', '*')
    return recipe

@app.route('/api/add-perishable')
def addPerishable(perishable_struct):
    perishables = perishable_struct["perishables"]
    for perishable in perishables:
        perishable.addToUserFood()
        perishable.addToFood()
    return "Added!"

@app.route('/api/new-recipe')
def getNewRecipe():

    return getNextRecipe()

@app.route('/api/suggestions')
def getSuggestions():
    return getPotentialIngredients()

@app.route('/api/upcoming-expiries')
def getUpcomingExpiries():
    return getUpcomingExpiryDates()

@app.route('/api/expired-foods')
def getExpired():
    return getExpiredFoods()

@app.route('/api/add-food/<item>/<exp>/<bought>/<amt>')
def addFood(item, exp, bought, amt):
    database = DataHandler()
    database.addUserFood(item, bought, exp, amt)



if __name__ == '__main__':
    app.run()
