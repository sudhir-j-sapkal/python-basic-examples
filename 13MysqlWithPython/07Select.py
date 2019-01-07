import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mypython_test_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee")

myresult = mycursor.fetchall()
print("**************All Records*******")
for x in myresult:
  print(x)

#Where Condition

sql1 = "SELECT * FROM employee WHERE address ='Pune'"

mycursor.execute(sql1)

myresult = mycursor.fetchall()
print("***********Records which satisfy where condition ***********")
for x in myresult:
  print(x)

print("**********Record which have 'a' in name************")
sql2 = "SELECT * FROM employee WHERE name LIKE '%ha%'"

mycursor.execute(sql2)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Prevent SQL Injection

print("**********Prevent SQL Injection******************************");
sql3 = "SELECT * FROM employee WHERE name = %s"
name = ("Salman Khan", )

mycursor.execute(sql3, name)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

print("********Order By**************");
sql4 = "SELECT * FROM employee ORDER BY name"
#To have DESC order give DESC after the name in above query
mycursor.execute(sql4)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

print("**************Delete Record************************")
sql5 = "DELETE FROM employee WHERE name = 'Amey Wagh'"
mycursor.execute(sql5)
mydb.commit()
#Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
#Notice the WHERE clause in the DELETE syntax: The WHERE clause specifies which record(s) that should be deleted. If you omit the WHERE clause, all records will be deleted!
print(mycursor.rowcount, "record(s) deleted")
