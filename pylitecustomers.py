#Author: Mark Warren
#Date: 23/01/2024
#Purpose: Designed with use of SQLlite to store and update customer records locally.

#Acknowledgments:

#Code was adapted from the tutorial provided by freeCodeCamp.org (credit to John Elder):
#https://www.youtube.com/watch?v=byHcYRpMgI4

#Their referred url link to their github:
#https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course

#A handy piece of code for clearing the screen provided by Grepper (credit to Expensive Eagle):
#https://www.codegrepper.com/code-examples/python/python+os.system+clear+screen

import sqlite3
import sys

from os import system, name

def clearpage():
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac/linux
    else:
        _ = system('clear')

def backtomainmenu():
    input("Enter anything to continue...")
    clearpage()
    options()

def menu():
    print ("Welcome to the PyLite Customer Database")
    print ("1. Show All Records")
    print ("2. Add Record")
    print ("3. Delete Record")
    print ("4. Find Record")
    print ("5. Ammend Record")
    print ("6. Reset Records")
    print ("7. Exit Program")

def options():
    menu()
    Option = 0

    while Option == 0:
        try:
            Option = int(input("Enter a option from the above:"))
            if Option < 1 or Option > 7:
                raise Exception
        except Exception:
            clearpage()
            print("Invalid Entered Choice. Choose from the available Options below.")
            menu()
            Option = 0

        else:
            if Option == 1:
                clearpage()
                show_all()
                backtomainmenu()

            elif Option == 2:
                clearpage()
                record(firstname(), lastname(), email())
                backtomainmenu()

            elif Option == 3:
                clearpage()
                delete_record(enterid())
                backtomainmenu()

            elif Option == 4:
                lookmenu()
                selectlookmenu()

            elif Option == 5:
                ammendmenu()
                selectammendmenu()

            elif Option == 6:
                ask()
                yesno()

            elif Option == 7:
                clearpage()
                sys.exit()

def ask():
    clearpage()
    print("Are you sure you wish to Create or Reset to default values in table database?")
    print("{:<10}".format("Y - Yes"), "{:<10}".format("N - No"))

def yesno():
    yn = None
    while yn not in ("yes", "no", "y", "n"):
        try:
            yn = str(input("Enter a option from the above:"))
            if yn.lower() not in ("yes", "no", "y", "n"):
                raise Exception
        except Exception:
            clearpage()
            print("Invalid Entered Choice. Choose from the available Options below.")
            yn = None
            ask()
        else:
            if yn.lower() == "yes" or yn.lower() == "y":
                create()
                print("Data has been reset.")
                backtomainmenu()
            elif yn.lower() == "no" or yn.lower() == "n":
                backtomainmenu()

def lookmenu():
    clearpage()
    print("How do you wish to search?")
    print("1. ID")
    print("2. First Name")
    print("3. Last Name")
    print("4. Email")
    print("5. Cancel")

def ammendmenu():
    clearpage()
    print("What do you wish to ammend?")
    print("1. First Name")
    print("2. Last Name")
    print("3. Email")
    print("4. Cancel")

def selectammendmenu():
    AmOption = 0
    while AmOption == 0:
        try:
            AmOption = int(input("Enter a option from the above:"))
            if AmOption < 1 or AmOption > 4:
                raise Exception
        except Exception:
            clearpage()
            print("Invalid Entered Choice. Choose from the available Options below.")
            ammendmenu()
            AmOption = 0

        else:
            if AmOption == 1:
                id= ammendenterid()
                first= firstname()
                ammend_firrecord(first,id)
                print("First Name of record: ", id, "has been changed to: ", first)
                backtomainmenu()
            if AmOption == 2:
                id = ammendenterid()
                last = lastname()
                ammend_lasrecord(last, id)
                print("Last Name of record: ", id, "has been changed to: ", last)
                backtomainmenu()
            if AmOption == 3:
                id = ammendenterid()
                mail = email()
                ammend_emarecord(mail, id)
                print("Email of record: ", id, "has been changed to: ", mail)
                backtomainmenu()
            if AmOption == 4:
                backtomainmenu()

def selectlookmenu():
    LookOption = 0
    while LookOption == 0:
        try:
            LookOption = int(input("Enter a option from the above:"))
            if LookOption < 1 or LookOption > 5:
                raise Exception
        except Exception:
            clearpage()
            print("Invalid Entered Choice. Choose from the available Options below.")
            lookmenu()
            LookOption = 0

        else:
            if LookOption == 1:
                look_record1((searchID()))
                backtomainmenu()
            if LookOption == 2:
                look_record2((searchFname()))
                backtomainmenu()
            if LookOption == 3:
                look_record3((searchSname()))
                backtomainmenu()
            if LookOption == 4:
                look_record4((email()))
                backtomainmenu()
            if LookOption == 5:
                backtomainmenu()

def create():
    connection = sqlite3.connect("customers.db")
    cursor = connection.cursor()

    cursor.execute("drop table IF EXISTS customers")
    cursor.execute("create table customers (first_Name text, last_Name text, email text)")

    customers_list = [
        ('Mark', 'Warren', 'mark@warren.com'),
        ('Womble', 'Warren', 'womble@warren.com'),
        ('Jake', 'Creed', 'jake@creed.com'),
        ('Tom', 'Little', 'tom@little.com'),
        ('Nancy', 'Drew', 'nancy@drew.com'),
    ]

    cursor.executemany("insert into customers values (?,?,?)", customers_list)

    connection.commit()

    connection.close()

def show_all():
    connection = sqlite3.connect("customers.db")
    cursor = connection.cursor()

    cursor.execute("SELECT rowid, * from customers")
    items = cursor.fetchall()
    print ("{:<6}".format("ID ") + "{:<26}".format("NAME") + "EMAIL")
    for item in items:
        print("{:<5}".format(item[0]) + " " + "{:<10}".format(item[1]) + " " + "{:<15}".format(item[2]) + item[3])

    connection.close

def record(first, last, email):
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    connection.commit()
    connection.close()

def look_record1(id):
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, * FROM customers WHERE rowid = (?)", (id,))
    items= cursor.fetchall()
    print("{:<6}".format("Row ") + "{:<26}".format("NAME ") + "EMAIL")
    for item in items:
        print("{:<5}".format(item[0]) + " " + "{:<10}".format(item[1]) + " " + "{:<15}".format(item[2]) + item[3])

def look_record2(first):
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()
    cursor.execute('SELECT rowid, * FROM customers WHERE first_name LIKE ?',(f'%{first}%',))
    items= cursor.fetchall()
    print("{:<6}".format("Row ") + "{:<26}".format("NAME ") + "EMAIL")
    for item in items:
        print("{:<5}".format(item[0]) + " " + "{:<10}".format(item[1]) + " " + "{:<15}".format(item[2]) + item[3])

def look_record3(last):
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()
    connection.execute("SELECT rowid, * FROM customers WHERE last_name LIKE ?",(f'%{last}%',))
    items= cursor.fetchall()
    print("{:<6}".format("Row ") + "{:<26}".format("NAME ") + "EMAIL")
    for item in items:
        print("{:<5}".format(item[0]) + " " + "{:<10}".format(item[1]) + " " + "{:<15}".format(item[2]) + item[3])

def look_record4(email):
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, * FROM customers WHERE email LIKE ?",(f'%{email}%',))
    items= cursor.fetchall()
    print("{:<6}".format("Row ") + "{:<26}".format("NAME ") + "EMAIL")
    for item in items:
        print("{:<5}".format(item[0]) + " " + "{:<10}".format(item[1]) + " " + "{:<15}".format(item[2]) + item[3])

def delete_record(id):
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()
    cursor.execute("DELETE from customers WHERE rowid = (?)", (id,))

    connection.commit()
    connection.close()

def ammend_firrecord(first, id):
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE customers SET first_name = ? WHERE rowid = ?", (first, id,))

    connection.commit()
    connection.close()

def ammend_lasrecord(last, id):
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE customers SET last_name = ? WHERE rowid = ?", (last, id,))

    connection.commit()
    connection.close()

def ammend_emarecord(email, id):
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE customers SET email = ? WHERE rowid = ?", (email, id,))

    connection.commit()
    connection.close()

def firstname():
    Fname = (input("Enter a First Name:"))
    TestFname = Fname.lower()
    valid = False

    while not valid:
        try:
            if TestFname.isalpha() and len(Fname)<11:
                valid = True
                return Fname
            else:
                raise ValueError
        except ValueError:
            print("First name must be valid or less than 10 characters long")
            Fname = (input("Enter a First Name:"))
            TestFname = Fname.lower()

def lastname():
    Sname = (input("Enter a Last Name:"))
    TestSname = Sname.lower()
    valid = False

    while not valid:
        try:
            if TestSname.isalpha() and len(Sname)<16:
                valid = True
                return Sname
            else:
                raise ValueError
        except ValueError:
            print("Last name must be valid or less than 15 characters long")
            Sname = (input("Enter a Last Name:"))
            TestSname = Sname.lower()

def email():
    Ename = (input("Enter an email:"))
    return Ename

def searchID():
    IDName = (input("Enter a ID:"))
    return IDName

def searchFname():
    Fname = (input("Enter a First Name:"))
    return Fname

def searchSname():
    Sname = (input("Enter a Last Name:"))
    return Sname

def ammendenterid():
    show_all()
    valid = False

    while not valid:
        try:
            IDName = (input("Enter a ID to ammend - please note: an error may occur if ID does not exist: (cancel to return to menu): "))
            IsCancel = IDName.lower()
            if IsCancel == "cancel":
                backtomainmenu()
            if len(str(IDName))<4 and int(IDName) > 0:
                return IDName
            else:
                raise ValueError
        except ValueError:
            print("The ID must be a valid number, an ID can not exceed 999.")


def enterid():
    show_all()
    valid = False

    while not valid:
        try:
            IDName = (input("Enter a ID to delete: (cancel to return to menu): "))
            IsCancel = IDName.lower()
            if IsCancel == "cancel":
                backtomainmenu()
            if len(str(IDName))<4 and int(IDName) > 0:
                print(IDName, " shall now be deleted.")
                return IDName
            else:
                raise ValueError
        except ValueError:
            print("The ID must be a valid number, an ID can not exceed 999.")

clearpage()
create()
options()