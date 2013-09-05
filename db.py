#coding=utf8

import _mysql
import os
import threading
import random
import time
import sys, getopt

"""
Run it: python db.py --mylog=/path/to/mysql/log
"""
config = {
	"path_to_mysql_log": "",
}

"""Print Usage Message"""
def print_usage():
	print """usage: python db.py --mylog=/path/to/mysql/log"""

def read_mylog():
	pass

def mysql_query_is_select(query):
	query = query.replace('\n', "")
	query_parts = query.split('\t')
	if len(query_parts) == 4 and query_parts[3] != "":
		time = query_parts[0]
		query_id = query_parts[2].split()
		if len(query_id) == 2 and query_id[1] == "Query":
			return True
	return False

def mysql_query_get_query_parts(query):
	query = query.replace('\n', "")
	tmp_parts = query.split('\t')
	# Hardcode here
	parts = []
	for part in tmp_parts:
		if part != "":
			parts.append(part)

	return parts

def mysql_query_is_update():
	pass

def mysql_query_is_delete():
	pass

def mysql_query_is_insert():
	pass

def run():

	# Step 1, Analysic query log 
	if not os.path.lexists(config["path_to_mysql_log"]):
		sys.stderr.write("The mysql log path is not exist\r\n");
		sys.exit(1)
	select_logs = []
	with open(config["path_to_mysql_log"]) as f:
		# ignore 3 lines
		comment = f.readline()
		port_info = f.readline()
		f.readline()
		for line in f:
			if mysql_query_is_select(line):
				select_logs.append(mysql_query_get_query_parts(line))

	# Step 3, Initialize thread pool


	


if __name__ == "__main__":
	try:
		args, unknownArgs = getopt.getopt(sys.argv[1:], "", ["mylog="])
	except getopt.GetoptError as err:
		sys.stderr.write("Exception because wrong options\r\n")
		print_usage()

	for n, v in args:
		if (n == "--mylog"):
			config["path_to_mysql_log"] = v;

	run()