import json
import time
import configparser
import random

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


eventCount=0

while True:
#        sleep_time=getEPS()
	start_time = time.time()
        for x in range(0,100):
                value = random.randint(0,0);
                action = actions[value];
                event_data = {'value':value,'action':action, 'timestamp':time.time()}
#		print event_data
		eventCount=eventCount+1
#		print eventCount
		try :
			response = requests.post("http://localhost:8080", json=event_data)
#			print response
		except Exception as ex:
			print ex
#		time.sleep(sleep_time)


	eventCount = eventCount + 100
	elapsed_time = time.time() - start_time

	print "EPS rate : {} ".format(100.0/elapsed_time)


