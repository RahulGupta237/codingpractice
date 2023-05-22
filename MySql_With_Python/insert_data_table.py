
import mysql.connector
try:

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database='Student'
    
    )

    mycursor = mydb.cursor()

    sql = 'INSERT INTO Detail_Student (name, address) VALUES(%s, %s)'
    val = ("Budiya", "Raxaul")
    mycursor.execute(sql, val)

    mydb.commit() # very important method to required changes like insert delete update 
except:
  
    mydb.rollback()
finally:
    print(mycursor.rowcount, "record inserted.")
    mycursor.close()
    mydb.close()