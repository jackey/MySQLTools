import time
import threading
import Queue

class CustomThreading(threading.Thread):
	def run(self):
		print "Thread: %s runing at %s." %(self.getName(), time.time())


hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com", "http://apple.com", "http://ibm.com"]

queue = Queue.Queue(len(hosts))

queue.join()

[queue.put(host) for host in hosts]

while True:
	try:
		host = queue.get()
		print "Host: %s " %(host)
	except EmptyError:
		sys.exit()
