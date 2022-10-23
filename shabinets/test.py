import mysql.connector
import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

mydb= mysql.connector.connect(
    host= os.environ["production_host"],
    user= os.environ["production_user"],
    password= os.environ["production_password"],
    database= os.environ["production_database"]
)
cursor = mydb.cursor()
cursor = mydb.cursor()

sql = "INSERT INTO food (id, food_name, units) VALUES (%s, %s, %s)"
val = (2, "test", "pounds")
cursor.execute(sql, val)
mydb.commit()