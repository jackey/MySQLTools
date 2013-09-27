#encoding=utf8

import MySQLdb
import sys
import os
import db
import db_schema
import io_test
import time

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(APP_PATH, "src"))

config = db.load_config()

if __name__ == "__main__":
	# Get Databae config and init database connection
	dbname = config.get("mysql", "database")
	user = config.get("mysql", "user")
	pwd = config.get("mysql", "pass")
	host = config.get("mysql", "host")
	table = config.get("loop", "table")

	try:
		db = MySQLdb.connect(host=host, user=user, passwd=pwd, db=dbname)
	except:
		sys.stderr.write("Connect Mysql Error. Please make sure you have right permission to connect it.")
		sys.exit(1)

	cursor = db.cursor()
	cursor.execute("desc %s" %(table))

	fields = []
	while True:
		field = cursor.fetchone()
		if not field:
			break
		if field[3] and "PRI" in field[3]:
			# It is primary key. So we don't need to auto generate value to it 
			pass
		else:
			fields.append((field[0], field[1]))
	cursor.close()

	loop = int(config.get("loop", "loop")) * 60
	timeout = 0
	cursor = db.cursor()
	while True:
		queries = io_test.general_insert_queries(table, fields, 1)
		cursor.execute(queries[0][1])
		db.commit()
		print "Inserted %d times. " %(timeout)
		# Loop in time that loop param says
		time.sleep(1)
		timeout += 1
		if timeout > loop:
			break;

	cursor.close()
	db.close()
		

