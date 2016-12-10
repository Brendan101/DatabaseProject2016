#!/usr/bin/python

# Lists all the database tables and allows user to erase one


import sqlite3 as lite
import sys

con = None

# Print usage
#if (len(sys.argv) != 3):
#	print("Usage:")
#	print("\t./bulk_load_csv.py <table_name> <path_to_csv>")


try:
	# Connecting
	con = lite.connect("db.project")
	cur = con.cursor()

	qry = "select name from sqlite_master where type = 'table';"

	# Executting
	cur.execute(qry)
	result = cur.fetchall()

	print("Tables:")
	count = 0
	
	table_array = []
	for t in result:
		count += 1
		
		table_array.append(t[0])
		output_string = str(count) + ") " + t[0]
		print(output_string)	

	user_input = input("Make a selection ")
	while(user_input < 1 or user_input > len(table_array)):
		user_input = input("Invalid.  Chose from above numbers. ")


	# Final Query:
	qry = "DELETE FROM " + table_array[user_input - 1] + ";"
	print(qry)

	cur.execute(qry)

	# Saving data inserts
	con.commit()
	con.close()

except:
	print("ERROR!  Exitting.")
	exit(-1)
