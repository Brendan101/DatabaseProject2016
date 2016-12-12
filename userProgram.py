#!/usr/bin/python
# -*- coding: utf-8 -*-


# ----------------------------------------------------------------
#
# userProgram.py  
#
# This program is part of the final project for CMSC461, Fall 2016
# taught by professor George Ray.
#
# Created by Group 3:
# James Alfano
# Domenick Powers
# Alex McCaslin
# Brendan Waters
# Sam Benas
#
# ----------------------------------------------------------------


import sqlite3 as lite
import sys

db_file = "db.project"


# Loads data from a CSV file

def bulkLoad():
    print("Bulk loading")
    csv_path = raw_input("Input your path to csv: ")

    #print("Attempting to read %s" % csv_path)

    table = raw_input("Input table: ")

    csv_file = open(csv_path, "r")   
 
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
        #print(insert_string)  # Debugging

        # Executting
        runSql(insert_string)

# Searches one table for a given value

def select():
    table = raw_input("What table? Office, CustomerAgencies, AgencyLocation, RentalAgreement, Manage: ")
    statement = ""

    if table == "Office":
        value = raw_input("office_name (or \"ALL\")? ")
        if value == "ALL":
            statement = "select * from " + table + ";"
        else:
            statement = "select * from " + table + " where office_name='" + value + "';"
    elif table == "CustomerAgencies":
        value = raw_input("agency_id (or \"ALL\")? ")
        if value == "ALL":
            statement = "select * from " + table + ";"
        else:
            statement = "select * from " + table + " where agency_id=" + value
    elif table == "AgencyLocation":
        value = raw_input("agency_city (or \"ALL\")? ")
        if value == "ALL":
            statement = "select * from " + table + ";"
        else:
            statement = "select * from " + table + " where agency_city=" + value
    elif table == "RentalAgreement":
        value = raw_input("rental_id (or \"ALL\")? ")
        if value == "ALL":
            statement = "select * from " + table + ";"
        else:
            statement = "select * from " + table + " where rental_id=" + value
    elif table == "Manage":
        value = raw_input("manage_id (or \"ALL\")? ")
        if value == "ALL":
            statement = "select * from " + table + ";"
        else:
            statement = "select * from " + table + " where manage_id=" + value

    print("") # For readability
    return statement


# Inserts one row into table

def insert():
    table = raw_input("What table? Office, CustomerAgencies, AgencyLocation, RentalAgreement, Manage: ")
    
    statement = ""

    if table == "Office":
        office_name = raw_input("Office_name: ")
        office_city = raw_input("Office city: ")
        office_sqft = raw_input("Office sqft: ")
        statement = "INSERT INTO Office VALUES (\'" + office_name + "\', \'" + office_city + "\', " + office_sqft + ");"
    elif table == "CustomerAgencies":
        agency_id = raw_input("What agency_id? ")
        agency_name = raw_input("agency_name? ")
        agency_city = raw_input("agency_city? ")
        phone_num = raw_input("phone_num? ")
        statement = "INSERT INTO CustomerAgencies VALUES (" + agency_id + ", \'" + agency_name + "\', \'" + agency_city + "\', \'" + phone_num + "\')"
    elif table == "AgencyLocation":
        agency_city = raw_input("What agency_city? ")
        agency_address = raw_input("agency_address? ")
        statement = "INSERT INTO AgencyLocation VALUES (\'" + agency_city + "\', \'" + agency_address + "\')"
    elif table == "RentalAgreement":
        rental_id = raw_input("What rental_id? ")
        rental_amount = raw_input("rental_amount? ")
        end_date = raw_input("end_date? ")
        statement = "INSERT INTO RentalAgreement VALUES (" + rental_id + ", " + rental_amount + ", \'" + end_date + "\')"
    elif table == "Manage":
        manage_id = raw_input("What manage_id? ")
        office_name = raw_input("office_name? ")
        agency_id = raw_input("agency_id? ")
        rental_id = raw_input("rental_id? ")
        statement = "INSERT INTO Manage VALUES (" + manage_id + ", \'" + office_name + "\', " + agency_id + ", " + rental_id + ")"

    return statement


# Deletes one row from a table

def delete():
    
    table = raw_input("What table? Office, CustomerAgencies, AgencyLocation, RentalAgreement, Manage: ")
    column = raw_input("What column? ")
    value = raw_input("What value? ")

    if not value.replace('.','',1).isdigit():
        value = "\'" + value + "\'"
    


    statement = "delete from " + table + " where " + column + "=" + value
    
    return statement


# Deletes all rows from a table

def erase():
    
    #table = raw_input("What table? ")
    table = raw_input("What table? Office, CustomerAgencies, AgencyLocation, RentalAgreement, Manage: ")

    
    statement = "DELETE FROM " + table + ";"
    return statement


# Used to execute SQL queries 

def runSql(statement):
    con = None
    
    try:
        con = lite.connect(db_file)
        cur = con.cursor()
        #print("Executing statement: " + statement) # Debugging
        cur.execute(statement)
        
        result = cur.fetchall()

        #if result:
        #    print(result)  # Debug

        for rec in result:
            for field in rec:
                print(field)
            print("") # newline
                
        
        print("Success!")
        print("")    

        con.commit()
        con.close()

        return 0
    
    
    except:
        print("ERROR! Invalid query.")
        #exit(-1)


# Loop to handle user menu

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
    tableSelection = input("Number: ")
    #print(tableSelection)   # For debugging

 
    if(tableSelection == 1):
        bulkLoad()
        #bulkLoad calls runSql itself
    else:
        if(tableSelection == 2):
            statement = select()     
        elif(tableSelection == 3):
            statement = insert()
        elif(tableSelection == 4):
            statement = delete()
        elif(tableSelection == 5):
            statement = erase()
        elif(tableSelection == 9):
            done = 1
        else:
            print("Enter a valid command")
   
        finished = runSql(statement)
