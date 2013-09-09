#coding=utf8

import _mysql
import os
import threading
import random
import time
import sys, getopt
import ConfigParser
import db

class ClientConsumeThread(threading.Thread):
	def __init__(self, queries):
		threading.Thread.__init__(self)
		self.queries = queries
		self.config = db.load_config()
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