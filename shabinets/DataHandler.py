import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

class DataHandler:
    mydb= mysql.connector.connect(
    host= os.environ["production_host"],
    user= os.environ["production_user"],
    password= os.environ["production_password"],
    database= os.environ["production_database"]
    )
    cursor = mydb.cursor()

    def __init__(self):
    
        self.cursor = self.mydb.cursor()
        self.cursor = self.mydb.cursor(buffered=True)

    def addFood(self, food_name, units):
        sql = "INSERT INTO food (food_name, units) VALUES (%s, %s, %s)"
        val = (food_name, units)
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def addRecipeIngredient(self, food_name, recipeId, amount, displayLine):
        sql = "INSERT INTO recipe_ingredient (food_name, recipe_id, amount, display_line) VALUES (%s, %s, %s)"
        val = (food_name, recipeId, amount, displayLine)
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def addUserFood(self, name, bought, expire, amount):
        sql = "INSERT INTO user_food (name, bought, expire, amount) VALUES (%s, %s, %s. %s)"
        val = (name, bought, expire, amount)
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def getRecipeByFood(self, perishableObjectName):
        recipeName = None
        recipeId = None
        recipePicture = None
        instructionsLink = None
        ingredientsList = []
        perishable = perishableObjectName
        query = ("select recipe_id from recipe_ingredient where food_name = %s")
        self.cursor.execute(query, (perishable,))
        for recipe_id in self.cursor:
            recipeId = recipe_id
            break
        if recipeId == None:
            return None
        query = "select recipe_name, instructions_link, pic_link from recipes where id = %s order by preference desc"
        self.cursor.execute(query, (recipeId))
        for recipe_name, instructions_link, pic_link, in self.cursor:
            recipeName = recipe_name
            recipePicture = pic_link
            instructionsLink = instructions_link
            break
        query = ("select display_line from recipe_ingredient where recipe_id = %s")
        self.cursor.execute(query, (recipeId))
        for display_line in self.cursor:
            ingredientsList.append(display_line)
            recipe_json = {
                "recipe": {
                    "label": recipeName,
                    "ingredients": ingredientsList,
                    "image": recipePicture,
                    "instructions": instructionsLink,
                    "id": recipeId
                }
            }
        return recipe_json
    
    def findNextExpired(self):
        foodName = None
        boughtId = None
        expireId = None
        foodAmount = None
        query = ("select food_name, bought_date, expire_date, amount from user_food where expire_date = (select min(expire_date) from user_food)")
        self.cursor.execute(query)
        for food_name, bought_date, expire_date, amount in self.cursor:
            foodName= food_name
            boughtId = bought_date
            expireId = expire_date
            foodAmount = amount
        return foodName

    def incrementPreference(self, recipeObjectID, increment):
        id = recipeObjectID
        sql = "UPDATE recipes SET preference = preference + %s WHERE id = %s"
        self.cursor.execute(sql,(increment, id))
        self.mydb.commit

    def getNextRecipeID():
        query = "SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'shabinets' AND TABLE_NAME = 'recipes'"
        self.cursor.execute(query)
        for AUTO_INCREMENT in self.cursor:
            id = AUTO_INCREMENT
            break

    def enterRecipe(self, jsonObject):
        for recipeDict in jsonObject["hits"]:
            id = getNextRecipeID
            name = recipeDict["recipe"]["label"]
            picLink = recipeDict["recipe"]["image"]
            IngredientList = ["ingredients"]
            instructionsLink = recipeDict["url"]
            sql = "INSERT INTO recipe (id, recipe_name, pic_link, instructions_link, preference) VALUES (%s, %s, %s. %s)"
            val = (id, name, picLink, instructionsLink, 0)
            self.cursor.execute(sql, val)
            self.mydb.commit()

            for ingredient in IngredientList:
                ingredientName = ingredient["food"]
                units = ingredient["measure"]
                displayLine = ingredient["text"]
                amount = ingredient["quantity"]
                self.addFood(ingredientName, units)
                self.addRecipeIngredient(ingredientName, id, amount, displayLine)
