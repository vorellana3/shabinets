import mysql.connector
from dotenv import load_dotenv
import os
from food import Food
from recipe import Recipe
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

  def addFood(self, id, food_name, units):
    sql = "INSERT INTO food (id, food_name, units) VALUES (%s, %s, %s)"
    val = (id, food_name, units)
    self.cursor.execute(sql, val)
    self.mydb.commit()

  def addUserFood(self, id, bought, expire, amount):
    sql = "INSERT INTO food (id, bought, expire, amount) VALUES (%s, %s, %s. %s)"
    val = (id, bought, expire, amount)
    self.cursor.execute(sql, val)
    self.mydb.commit()

  def getJsonRecipe(self, perishable):
    recipeName = None
    recipeId = None
    recipePicture = None
    instructionsLink = None
    ingredientsList = []
    query = ("select recipe_id from recipe_ingredient where food_id = (select food_id from food where food_name = %s)")
    self.cursor.execute(query, (perishable))
    for recipe_id in self.cursor:
      recipeId = recipeId
      break
    query = "select recipe_name, instructions_link, pic_link from recipe where id = %s"
    self.cursor.execute(query, (recipeId))
    for recipe_name, instructions_link, pic_link in self.cursor:
      recipeName = recipe_name
      recipePicture = pic_link
      instructionsLink = instructions_link
      break
    query = ("select display_line from recipe where recipe_id = %s")
    self.cursor.execute(query, (recipeId))
    for display_line in self.cursor:
      ingredientsList.append(display_line)
    recipe = Recipe(recipeName, recipePicture, recipeId, ingredientsList, instructionsLink)
    return recipe.getJson
    
  def findNextExpired(self):
    FoodId = None
    foodName = None
    boughtId = None
    expireId = None
    foodAmount = None
    query = ("select food_id, bought_id, expire_date, amount from user_food where expire_date = min(expire_date)")
    self.cursor.execute(query)
    for food_id, bought_id, expire_date, amount in self.cursor:
      foodId= food_id
      boughtId = bought_id
      expireDate = expire_date
      foodAmount = amount
    nameQuerry = ("select name from food where food_id = (select food_id from user_food order by expire_date limit 1)")
    self.cursor.execute(nameQuerry)
    for name in self.cursor:
      foodName = name
    food = Food(foodName, foodId, boughtId, expireId, foodAmount)