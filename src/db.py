#coding=utf8

import _mysql
import os
import threading
import random
import time
import sys, getopt
import ConfigParser

PWD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""
Run it: python db.py --mylog=/path/to/mysql/log
"""

class ClientConsumeThread(threading.Thread):
	def __init__(self, queries):
		threading.Thread.__init__(self)
		self.queries = queries
		self.config = load_config()
		self.db = _mysql.connect(self.config.get("mysql", "host"), \
				self.config.get('mysql', 'user'), \
				self.config.get('mysql', 'pass'), \
				self.config.get('mysql', 'database'))

	def run(self):
		for query in self.queries:
			sql = query[1]
			try:
				self.db.query(sql)
				result = self.db.store_result()
				print "Run: %s" %(sql)
			except Exception as e:
				print "Error: %s" %(sql)

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

	threads_queue = []
	thread_pool_size = config.get("threadpool", "poolsize")
	for i in range(1, int(thread_pool_size)):
		thread = ClientConsumeThread(select_logs)
		print "Thread: %s created" %(thread.getName())
		threads_queue.append(thread)

	for client in threads_queue:
		client.start()

	for client in threads_queue:
		client.join()

	print "Finished"


config = load_config()

if __name__ == "__main__":
	run()