import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mypython_test_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO employee (name, address) VALUES (%s, %s)"
val = ("Rohan", "Jhakle")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
