#coding=utf8

import re
import string
import random

def is_int(str):
	return re.search("int", str)

def is_char(str):
	return re.search("char", str)

def is_date(str):
	return re.search("date", str)

def random_str(long):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(long))

def random_int(upper_limit):
	return random.randint(upper_limit>>1, upper_limit<<1)