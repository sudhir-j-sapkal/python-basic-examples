import mysql.connector
#Create Connection to DB
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mypython_test_db"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE employee (name VARCHAR(255), address VARCHAR(255))")
