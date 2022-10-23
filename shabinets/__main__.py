from flask import Flask, jsonify
import json
from recipes_access import getNextRecipe, getAllRecipes
from flask_cors import CORS, cross_origin

app = Flask("shabinets")
CORS(app)

@app.route('/<food>')

def index(food):
    recipe = getNextRecipe(food)#.headers.add('Access-Control-Allow-Origin', '*')
    return recipe

app.run()
