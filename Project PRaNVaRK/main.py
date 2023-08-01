import mysql.connector as sql
import csv
import os
from prettytable import PrettyTable

#User Login Module ----COMPLETED----
def user_login(): 
    os.system("cls")
    #admin = 2; user is 1; viewer is 0
    uname = input("Enter the user name: ")
    pwd = input("Enter the password: ")
    mycursor.execute("select role from users where name = '{}' and password = '{}'".format(uname, pwd))
    result = mycursor.fetchall()
    if (result == []):
        print("Invalid userid or password!!Please check")
    else:
        if (result[0][0] == 'ADMIN'):
            return 2
        elif(result[0][0] == 'USER'):
            return 1
        elif(result[0][0] == 'VIEWER'):
            return 0
    return 99

#view_stocks() here --Completed--
def view_stocks():
    os.system("cls")
    print("1. View all Stocks")
    print("2. Search by Medicine Name")
    inp_viw_stck = int(input("Enter your choice(1/2): "))
    if (inp_viw_stck == 1):
        mycursor.execute("select * from stock")
        rslt_viw_stck = mycursor.fetchall()
        x = PrettyTable()
        x.field_names = x.field_names = ["Medicine Name", "Brand Name", "Price", "Quantity"] 
        x.add_rows(rslt_viw_stck)
        print(x)
    elif(inp_viw_stck == 2):
        mnme = input("Enter the medicine name: ")
        mycursor.execute("select * from stock where mname = '{}'".format(mnme))
        rslt = mycursor.fetchall()
        if (rslt == []):
            print("No record with such information found!!")
        else:
            x = PrettyTable()
            x.field_names = ["Medicine Name", "Brand Name", "Price", "Quantity"]
            for i in rslt:
                x.add_rows(rslt)
            print(x)
    else:
        print("Invalid Input!!")


def add_items_stocks():
    os.system("cls")
    mna = input("Enter the Medicine Name: ")
    bna = input("Enter the Brand Name: ")
    price = int(input("Enter the Price: "))
    quantity = int(input("Enter the Quantity: "))
    mycursor.execute("insert into stock values(%s, %s, %s, %s)",(mna.lower(), bna.lower(), int(price), int(quantity)))
    mydb.commit()
    print("Item added successfully!!")


def del_items_stocks():
    os.system("cls")
    mna = input("Enter the medicine name: ").lower()
    mycursor.execute("select * from stock where mname = '{}'".format(mna))
    result = mycursor.fetchall()
    if (result == []):
        print("The following medicine doesn't exist in the database")
    else:
        mycursor.execute("delete from stock where mname = '{}'".format(mna))
        mydb.commit()
        print("The Medicine '{}' has been deleted from the database".format(mna))


def modify_items_stocks():
    os.system("cls")
    print("1.Medicine Name")
    print("2.Brand Name")
    print("3.Price")
    print("4.Quantity")
    old_mname = input("Enter the old Medicine Name: ")
    mycursor.execute("select * from stock where mname = '{}'".format(old_mname))
    rst = mycursor.fetchall()
    if (rst == []):
        print("The Medicine {} doesn't exists in the database".format(old_mname))
    else:
        result = int(input("Enter Column Number to be modified(1/2/3/4): "))
        if (result == 1):
            n_mname = input("Enter the new Medicine Name: ")
            mycursor.execute("update stock set Mname = '{}' where mname = '{}'".format(n_mname, old_mname))
            mydb.commit()
            print("Changes Updated in the Database")
        elif (result == 2):
            n_bname = input("Enter the new Brand Name: ")
            mycursor.execute("update stock set bname = '{}' where mname = '{}'".format(n_bname, old_mname))
            mydb.commit()
            print("Changes Updated in the Database")
        elif (result == 3):
            n_price = int(input("Enter the new price: "))
            mycursor.execute("update stocks set price = {} where mname = '{}'".format(n_price, old_mname))
            mydb.commit()
            print("Changes Updated in the Database")
        elif (result == 4):
            n_quantity = int(input("Enter the new quantity: "))
            mycursor.execute("update stock set quantity = {} where mname = '{}'".format(n_quantity, old_mname))
            mydb.commit()
            print("Changes Updated in the Database")
        else:
            print("Invalid Input!!Please check and try again")

def stock_main_menu():
    os.system("cls")
    print("1. View Stocks")
    print("2. Add Items in Stocks")
    print("3. Remove Items in Stock")
    print("4. Modify Item Properties in Stocks")
    stock_main_inp = int(input("Enter your input(1/2/3/4)"))
    if (stock_main_inp == 1):
        view_stocks()
    elif (stock_main_inp == 2):
        add_items_stocks()
    elif (stock_main_inp == 3):
        del_items_stocks()
    elif (stock_main_inp == 4):
        modify_items_stocks()


def view_user():
    os.system("cls")
    print("1. View all Users")
    print("2. Search by User Name")
    inp_viw_stck = int(input("Enter your choice(1/2): "))
    if (inp_viw_stck == 1):
        mycursor.execute("select * from users")
        rslt_viw_stck = mycursor.fetchall()
        x = PrettyTable()
        x.field_names = ["Username", "Role", "Password"]
        x.add_rows(rslt_viw_stck)
        print(x)
    elif(inp_viw_stck == 2):
        mnme = input("Enter the username: ")
        mycursor.execute("select * from users where name = '{}'".format(mnme))
        rslt = mycursor.fetchall()
        if (rslt == []):
            print("No record with such information found!!")
        else:
            x = PrettyTable()
            x.field_names = ["Username", "Role", "Password"]
            for i in rslt:
                x.add_rows(rslt)
            print(x)
    else:
        print("Invalid Input!!")


def add_user():
    os.system("cls")
    uname = input("Enter the username: ")
    print("User Role Relations")
    print("ADMIN")
    print("USER")
    print("VIEWER")
    role = input("Enter the role for the user: ")
    if (role not in ["ADMIN", "USER", "VIEWER"]):
        print("Invalid input! Please Try Again")
    else:
        pwd = input("Enter the password for the user: ")
        mycursor.execute("insert into users values('{}', '{}', '{}')".format(uname, role, pwd))
        mydb.commit()
        print("User Added!!")

def dlt_user():
    os.system("cls")
    uname = input("Enter the username to be deleted from the database:")
    mycursor.execute("select * from users where name = '{}'".format(uname))
    rst = mycursor.fetchall()
    if (rst == []):
        print("The username does not exist in the database")
    else:
        mycursor.execute("delete from users where name = '{}'".format(uname))
        mydb.commit()
        print("The user {} has from deleted from the database".format(uname))

def mod_user():
    os.system("cls")
    print("name")
    print("Role")
    print("Password")
    clm = input("Enter the column name to be modified: ")
    uname = input("Enter the username to be modified: ")
    mycursor.execute("select * from users where name = '{}'".format(uname))
    rslt = mycursor.fetchall()
    if (rslt == []):
        print("The record for the username doesnot exist")
    else:
        newval = input("Enter the new data: ")
        mycursor.execute("update users set {} = '{}' where name = '{}'".format(clm, newval, uname))
        mydb.commit()
        print("The data has been modified")

def user_main_menu():
    os.system("cls")
    if (role != 2):
        print("The user does not have permission to access this module")
    else:
        print("1. View Users")
        print("2. Add User")
        print("3. Delete User")
        print("4. Modify User Information(including Role change)")
        slct = int(input("Enter your choice(1/2/3/4): "))
        if (slct == 1):
            view_user()
        elif (slct == 2):
            add_user()
        elif (slct == 3):
            dlt_user()
        elif (slct == 4):
            mod_user()
        else:
            print("Incorrect Option Selected!!Please try again!")


filename = "sql_user_data.csv"
with open(filename, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    for a in csvread:
        un = a[0]
        pwd = a[1]
        break
mydb = sql.connect(host = "localhost", user = "{}".format(un), password = "{}".format(pwd))
mycursor = mydb.cursor()
mycursor.execute("use PRaNVaRK")
role = user_login() #login with various roles ----COMPLETED----
if (role == 99):
    print("Access not granted!!")
else:
    os.system("cls")
    while True:
        print("---Main Menu---")
        print("1.Stock Management")
        print("2. User Management")
        print("3. Quit")
        main_inp = int(input("Enter your choice(1/2/3): "))
        if (main_inp == 1):
            stock_main_menu()
        elif (main_inp == 2):
            user_main_menu()
        elif (main_inp == 3):
            break
        else:
            print("Invalid Input! Please try again")
