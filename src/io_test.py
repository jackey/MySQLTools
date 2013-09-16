#encoding=utf8

import os, sys
import db
import _mysql

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(APP_PATH, "src"))



if __name__ == "__main__":
	config = db.load_config()