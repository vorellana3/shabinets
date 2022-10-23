import pandas as pd

class RecipeIngredient:
    foodID = 0
    recipeID = 0
    amount = 0


    def __init_(foodID, recipeID, amount):
        self.foodID = foodID
        self.recipeID = recipeID
        self.amount = amount
