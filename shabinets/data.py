import pandas as pd

class Data:
    food = pd.DataFrame(data = [])
    recipes = pd.DataFrame(data = [])
    recipe_ingredients = pd.DataFrame(data = [])
    user_food = pd.DataFrame(data = [])

    def __init__(
