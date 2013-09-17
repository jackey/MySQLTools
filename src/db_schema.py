#coding=utf8

import re
import string
import random

lenre = re.compile("\d+")

def is_int(str):
	return re.search("int", str), lenre.findall(str)[0]

def is_char(str):
	return re.search("char", str), lenre.findall(str)[0]

def is_date(str):
	return re.search("date", str)

def random_str(long):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(long))

def random_int(upper_limit):
	return random.randint(upper_limit>>1, upper_limit<<1)

def field_value(field_type):
	isint, intlen = is_int(field_type)
	ischar, charlen = is_char(field_type)

	if isint is not None:
		print random_int(1<<int(intlen)*4)
	elif ischar is not None:
		pass


