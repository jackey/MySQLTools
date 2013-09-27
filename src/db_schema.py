#coding=utf8

import re
import string
import random
import datetime

lenre = re.compile("\d+")

def is_int(str):
	results = lenre.findall(str)
	return re.search("int", str), results[0] if len(results) > 0 else 10

def is_char(str):
	results = lenre.findall(str)
	return re.search("char", str), results[0] if len(results) > 0 else 10

def is_date(str):
	return re.search("date", str)

def is_blob(str):
	return re.search("blob", str), 1000

def random_str(long):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(long))

def random_int(upper_limit):
	return random.randint(upper_limit>>1, upper_limit<<1)

def field_value(field_type):
	isint, intlen = is_int(field_type)
	ischar, charlen = is_char(field_type)
	isblob, bloblen = is_blob(field_type)


	if isint is not None:
		return random_int(1<<int(intlen))
	elif ischar is not None:
		return random_str(int(charlen))
	elif isblob is not None:
		return random_str(int(bloblen))
	elif isdate is not None:
		return "2013-09-24"


