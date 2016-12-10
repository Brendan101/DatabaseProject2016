#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys

def bulkLoad():
    csv_file = input("Input your path to csv:")
    table = input("Input table")
    
    for line in csv_file:

        # Clear newline
        line = line.strip("\n")
            
        data_list = line.split(',')

        # Beginning string
        insert_string = "INSERT INTO " + table + " VALUES ("

        # Constructing string
        count = 0
        for d in data_list:    
            count += 1
    
            # Trick to turn floats to ints to run isdigit
            # Do not want single quotes for numeric values
            if(d.replace('.','',1).isdigit()):
                insert_string += str(d)
            else:
                insert_string += "\'" + d + "\'"
    
            # Add comma if not final item in list    
            if (count < len(data_list) ):
                insert_string += ","


        insert_string += ");"
        print(insert_string)  # Debugging

        # Executting
        runSql(insert_string)

def select():
    table = input("What table? Office, CustomerAgencies, AgencyLocation, RentalAgreement, Manage")
    statement = ""

    if table == "Office":
        value = input("What office_name?")
        statement = "select * from " + table + " where office_name='" + value + "';"
    elif table == "CustomerAgencies":
        value = input("What agency_id?")
        statement = "select * from " + table + " where agency_id=" + value
    elif table == "AgencyLocation":
        value = input("What agency_city?")
        statement = "select * from " + table + " where agency_city=" + value
    elif table == "RentalAgreement":
        value = input("What rental_id?")
        statement = "select * from " + table + " where rental_id=" + value
    elif table == "Manage":
        value = input("What manage_id?")
        statement = "select * from " + table + " where manage_id=" + value

    return statement

def insert():
    table = input("What table? Office, CustomerAgencies, AgencyLocation, RentalAgreement, Manage")
    
    statement = ""

    if table == "Office":
        office_name = input("What office_name?")
        office_city = input("What office city")
        office_sqft = input("Office sqft?")
        statement = "INSERT INTO Office VALUES (" + office_name + ", " + office_city + ", " + office_sqft + ")"
    elif table == "CustomerAgencies":
        agency_id = input("What agency_id?")
        agency_name = input("agency_name?")
        agency_city = input("agency_city?")
        phone_num = input("phone_num?")
        statement = "INSERT INTO CustomerAgencies VALUES (" + agency_id + ", " + agency_name + ", " + agency_city + ", " + phone_num + ")"
    elif table == "AgencyLocation":
        agency_city = input("What agency_city?")
        agency_address = input("agency_address?")
        statement = "INSERT INTO AgencyLocation VALUES (" + agency_city + ", " + agency_address + ")"
    elif table == "RentalAgreement":
        rental_id = input("What rental_id?")
        rental_amount = input("rental_amount?")
        end_date = input("end_date?")
        statement = "INSERT INTO RentalAgreement VALUES (" + rental_id + ", " + rental_amount + ", " + end_date + ")"
    elif table == "Manage":
        manage_id = input("What manage_id?")
        office_name = input("office_name?")
        agency_id = input("agency_id?")
        rental_id = input("rental_id?")
        statement = "INSERT INTO Manage VALUES (" + manage_id + ", " + office_name + ", " + agency_id + ", " + rental_id + ")"

    return statement

def delete():
    
    table = input("What table? Office, CustomerAgencies, AgencyLocation, RentalAgreement, Manage")
    column = input("What column?")
    value = input("What value?")
    statement = "delete from " + table + " where " + column + "=" + value
    
    return statement

def erase():
    
    table = input("What table?")
    
    statement = "DELETE FROM " + table + ";"
    return statement

def runSql(statement):
    con = None
    
    try:
        con = lite.connect("soap.sql")
        print(con)
        cur = con.cursor()
        print(cur)
        print(statement)
        cur.execute(statement)
        print("Hello")
        result = cur.fetchall()
        print(result)
        for rec in result:
            for field in rec:
                print(field)
                
        print("Success!")
    
        con.commit()
        con.close()

        return 0
    
    
    except:
        print("ERROR!  Exitting.")
        exit(-1)


done = 0

while(done == 0):
    print("What task do you want to do?")
    print("1. Bulk load csv")
    print("2. Select from table")
    print("3. Insert into table")
    print("4. Delete from table")
    print("5. Erase table")
    print("9: Quit")

    statement = ""
    tableSelection = input(":")
    
    if(tableSelection == "1"):
        statement = bulkLoad()
    elif(tableSelection == "2"):
        statement = select()     
    elif(tableSelection == "3"):
        statement = insert()
    elif(tableSelection == "4"):
        statement = delete()
    elif(tableSelection == "5"):
        statement = erase()
    elif(tableSelection == "9"):
        done = 1
    else:
        print("Enter a valid command")
    
    finished = runSql(statement)
