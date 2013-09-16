#coding=utf8

import os, sys
import db
import MySQLdb

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(APP_PATH, "src"))

if __name__ == "__main__":
	config = db.load_config()
	try:
		db = MySQLdb.connect(host="localhost", user="root", passwd="admin", db="test_io")
	except MySQLdb.Error as e:
		print "Error: %d: %s" %(e.args[0], e.args[1])
		sys.exit(1)

	cursor = db.cursor()

	cursor.execute("""
		desc node
		""")

	while 1:
		row = cursor.fetchone()
		if not row:
			break
		print row

	cursor.close()
	db.close()