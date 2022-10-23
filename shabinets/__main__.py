from flask import Flask, jsonify
from food import Food
import json
from recipe import getRecipe, getAllRecipes, getNextRecipe
from flask_cors import CORS, cross_origin
import DataHandler

app = Flask("shabinets")
CORS(app)

@app.route('/')
def index():
    return "Hello world"

@app.route('/search/<food>')

def search(food):
    recipe = getNextRecipe(food)#.headers.add('Access-Control-Allow-Origin', '*')
    return recipe

@app.route('/add-perishable')
def addPerishable(perishable_struct):
    perishables = perishable_struct["perishables"]
    for perishable in perishables:
        perishable.addToUserFood()
        perishable.addToFood()
    return "Added!"

@app.route('/new-recipe')
def getNewRecipe():

    return getNextRecipe()


app.run()
