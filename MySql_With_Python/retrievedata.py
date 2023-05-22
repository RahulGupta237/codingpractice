
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="password",
database='Student'

)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM Detail_Student")

myresult = mycursor.fetchall()
lastid=mycursor.lastrowid
print(lastid)

for x in myresult:
  print("rahul retrieve",x)


  """

  Additionally, you can use apt-get update && apt-get upgrade to do both steps one after the other.
mysql -u root -p
password

  
  
  """