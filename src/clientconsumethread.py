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
	def __init__(self, queries, config = None, config_section="mysql"):
		threading.Thread.__init__(self)
		self.queries = queries
		self.config = config
		self.config_section = config_section
		if self.config is None:
			self.config = db.load_config()
		self.db = _mysql.connect(self.config.get(config_section, "host"), \
				self.config.get(config_section, 'user'), \
				self.config.get(config_section, 'pass'), \
				self.config.get(config_section, 'database'))

	def run(self):
		for query in self.queries:
			sql = query[1]
			try:
				self.db.query(sql)
				#result = self.db.store_result()
				if self.config.get(self.config_section, "print_to_console") == 0:
					print "Run: %s" %(sql)
			except Exception as e:
				if self.config.get(self.config_section, "print_to_console") == 0:
					print "Error: %s" %(sql)
