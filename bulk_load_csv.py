#!/usr/bin/python

# Bulk Loads from a CSV
# The csv must have values in the correct order, without column headers



import sqlite3 as lite
import sys

con = None

# Print usage
if (len(sys.argv) != 3):
	print("Usage:")
	print("\t./bulk_load_csv.py <table_name> <path_to_csv>")



# Connecting
try:
	con = lite.connect("db.project")
	cur = con.cursor()

	try:
		csv_file = open(sys.argv[2], "r")
	except:
		print("ERROR!  Could not open CSV!")
		exit(-1)
	
	for line in csv_file:

		# Clear newline
		line = line.strip("\n")
			
		data_list = line.split(',')

		# Beginning string
		insert_string = "INSERT INTO " + sys.argv[1] + " VALUES ("

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
		cur.execute(insert_string)

	# Saving data inserts
	con.commit()
	con.close()
except:
	print("ERROR!  Database malfunction!")
	exit(-2)
