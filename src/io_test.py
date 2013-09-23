#coding=utf8

import os, sys
import db
import MySQLdb
import db_schema
import clientconsumethread
import datetime

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(APP_PATH, "src"))

def general_insert_queries(table, fields, count = 1000):
	queries = []
	for i in range(0, count):
		values = []
		columns = []
		for field_name, field_type in fields:
			values.append("'"+ str(db_schema.field_value(field_type)) + "'")
			columns.append(field_name)
		queries.append(("", "INSERT INTO %s ( %s ) VALUES (%s)" %(table, ",".join(columns), ",".join(values))))
	return queries

if __name__ == "__main__":
	config = db.load_config()
	table = config.get("io_test_mysql", "table")
	database = config.get("io_test_mysql", "database");
	consume_count = config.get('io_test_mysql', 'consume')

	try:
		db = MySQLdb.connect(host="localhost", user="root", passwd="admin", db=database)
	except MySQLdb.Error as e:
		print "Error: %d: %s" %(e.args[0], e.args[1])
		sys.exit(1)

	cursor = db.cursor()

	cursor.execute("""desc %s""" %(table))

	fields = []
	while True:
		field = cursor.fetchone()
		if not field:
			break
		[name for name in field if name == "PRI"]
		if name is "":
			fields.append((field[0], field[1]))
	cursor.close()
	db.close()

	queries = general_insert_queries(table, fields, int(config.get("io_test_mysql", "count")))
	threads = []
	for i in range(int(consume_count)):
		 thread = clientconsumethread.ClientConsumeThread(queries, config, "io_test_mysql")
		 threads.append(thread)

	print "Start Running at: %s " %(datetime.datetime.now())
	for thread in threads:
		thread.start()
		print "Start Consume with name: %s." %(thread.getName())

	for thread in threads:
		thread.join()


	print "Finished at: %s " %(datetime.datetime.now())
