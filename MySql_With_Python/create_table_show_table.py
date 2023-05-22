import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database='Student'
  
)


mycursor = mydb.cursor()
### create table in student database   ####################
# mycursor.execute("CREATE TABLE Detail_Student (name VARCHAR(255), address VARCHAR(255))")

# print("Successfully created Table")


######################################
print(mydb.is_connected())
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

mycursor.close()
mydb.close()

