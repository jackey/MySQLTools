#coding=utf8

import os, sys
import db
import MySQLdb
import db_schema

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(APP_PATH, "src"))

def general_insert_queries(table, fields, count = 1000):
	values = []
	for field in fields:
		field_type = field[1]
		values.append(db_schema.field_value(field_type))
	pass

table = "node"
database = "test_io"

if __name__ == "__main__":
	config = db.load_config()
	try:
		db = MySQLdb.connect(host="localhost", user="root", passwd="admin", db=database)
	except MySQLdb.Error as e:
		print "Error: %d: %s" %(e.args[0], e.args[1])
		sys.exit(1)

	cursor = db.cursor()

	cursor.execute("""desc %s""" %(table))

	fields = []
	while 1:
		field = cursor.fetchone()
		if not field:
			break
		fields.append((field[0], field[1]))

	queries = general_insert_queries(table, fields)
	print queries
	cursor.close()
	db.close()