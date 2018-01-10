import json
import time
import configparser
import random
import thread
import requests

actions = ("BLOCK","ALLOW","TRUST");

def getEPS():
        config = configparser.ConfigParser()
        config.read('events.ini')
        eps = float(config['DEFAULT']['events_per_sec'])
        sleep_time = 1.0/eps
        return sleep_time


data = {
	"action":   "TRUST",
	"value": 2,
	"timestamp" : time.time()
}



def generateEvents(threadName):
	eventCount = 0
	while True:
	#        sleep_time=getEPS()
		start_time = time.time()
		for x in range(0,100):
			value = random.randint(0,0);
			action = actions[value];
			event_data = {'value':value,'action':action, 'timestamp':time.time()}
	#		print event_data
			try :
				response = requests.post("http://18.217.182.244:8080", json=event_data)
	#			print response
			except Exception as ex:
				print ex
	#		time.sleep(sleep_time)


		eventCount = eventCount + 100
		elapsed_time = time.time() - start_time

		print "{} EPS rate : {} ".format(threadName, 100.0/elapsed_time)

generateEvents("Non-threaded")

# Uncomment section below to run threaded.  
#------------------------------------------------------------
#thread.start_new_thread(generateEvents, ("thread-1",))
#thread.start_new_thread(generateEvents, ("thread-2",))
#thread.start_new_thread(generateEvents, ("thread-3",))
#thread.start_new_thread(generateEvents, ("thread-4",))
#thread.start_new_thread(generateEvents, ("thread-5",))
#thread.start_new_thread(generateEvents, ("thread-6",))
#thread.start_new_thread(generateEvents, ("thread-7",))
#thread.start_new_thread(generateEvents, ("thread-8",))
#thread.start_new_thread(generateEvents, ("thread-9",))
#thread.start_new_thread(generateEvents, ("thread-10",))
#while True:
#	pass
#------------------------------------------------------------

