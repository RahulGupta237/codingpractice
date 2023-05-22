import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

mycursor = mydb.cursor()
#### Create database Student name ##########################################
# mycursor.execute("CREATE DATABASE Student")
# print("Successfully created")
##################################################
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)