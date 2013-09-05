#coding=utf8

import _mysql
import os
import threading
import random
import time
import sys, getopt
import ConfigParser

PWD = os.path.dirname(os.path.abspath(__file__))

"""
Run it: python db.py --mylog=/path/to/mysql/log
"""

def load_config():
	path = os.path.join(PWD, "config.ini")
	if os.path.lexists(path):
		parser = ConfigParser.RawConfigParser()
		parser.read(path)
		return parser
	else:
		return False

def print_usage():
	"""Print Usage Message"""
	print """usage: python db.py --config=/path/to/config.ini"""

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
	[parts.append(part) for part in tmp_parts if part != ""]

	return parts

def mysql_query_is_update():
	pass

def mysql_query_is_delete():
	pass

def mysql_query_is_insert():
	pass

def callback_run_mysql_select(queries, time=3):
	"""Run mysql query in select type with times in param specialize"""
	for i in range(0, time):
		pass

def run():
	path_to_mysql_log = config.get("mysql", "log")
	# Step 1, Analysic query log 
	if not os.path.lexists(path_to_mysql_log):
		sys.stderr.write("The mysql log path is not exist\r\n");
		sys.exit(1)
	select_logs = []
	with open(path_to_mysql_log) as f:
		# ignore 3 lines
		comment = f.readline()
		port_info = f.readline()
		f.readline()
		[select_logs.append(mysql_query_get_query_parts(line)) for line in f if mysql_query_is_select(line)]

	# Step 3, Initialize thread pool

	print select_logs

config = load_config()

if __name__ == "__main__":
	try:
		args, unknownArgs = getopt.getopt(sys.argv[1:], "c:", ["config="])
		if len(args)  == 0:
			print_usage()
			sys.exit(1)
	except getopt.GetoptError as err:
		sys.stderr.write("Exception because wrong options\r\n")
		print_usage()
		sys.exit(1)

	for n, v in args:
		if (n == "--mylog"):
			config["path_to_mysql_log"] = v;

	run()