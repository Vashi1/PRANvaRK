import os
import csv
filename = "sql_user_data.csv"
import mysql.connector as sql
mydb = sql.connect(host = 'localhost', user = 'root', password = 'Rakshith1@')
mycursor = mydb.cursor()
#Adding the database and related tables
mycursor.execute("create database PRaNVaRK")
mycursor.execute("use PRaNVaRK")
mycursor.execute("create table Users(name char(255), role char(255))")
mycursor.execute("insert into Users values ('admin', 'ADMIN', 'admin')")
mycursor.execute("insert into Users values ('abc', 'USER', 'abc')")
mycursor.execute("create table stock (mname char(255), bname char(255), price int(255), quantity int(255))")
#Adding username and password for the end-user
while (True):
    print("Enter the user name for sql user: ")
    a = input()
    print("Enter the password for sql user ",  a)
    b = input()
    print("The username is ", a)
    print("The password is ", b)
    print("Do you want to continue(y/n): ")
    c = input()
    if (c.lower().strip() == "y"):
        mycursor.execute("create user '{}'@'localhost' identified by '{}'".format(a, b))
        mycursor.execute("grant all privileges on pranvark.* to '{}'@localhost".format(a))
        rows = [a, b]
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(rows) 
        break
    else:
        print("Plese enter the details again")
        os.system('cls')
