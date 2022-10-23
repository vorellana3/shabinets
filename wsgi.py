from flask import Flask, jsonify
from shabinets import Food, getRecipe, getAllRecipes, getNextRecipe
import json
from flask_cors import CORS, cross_origin

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
        Food.addToUserFood(perishable)
    return "Added!"

@app.route('/api/new-recipe')
def getNewRecipe():

    return getNextRecipe()

if __name__ == '__main__':
    app.run()
