import mysql.connector as sql

mydb = sql.connect(host="localhost", user='root', password="Rakshith1@")
print(mydb)

mycursor = mydb.cursor()
mycursor.execute("use PRaNVaRK")
mycursor.execute("show tables")
for x in mycursor:
    print(x)