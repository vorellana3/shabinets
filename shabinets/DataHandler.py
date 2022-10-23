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

