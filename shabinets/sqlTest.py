import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "test",
    database = "shabinets"
)
 
# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()
 
# Show database
cursor.execute("SHOW TABLES")
 
for x in cursor:
  print(x)