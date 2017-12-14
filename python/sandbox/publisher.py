import json
import urllib2
import time
import configparser
import random

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

req = urllib2.Request('http://localhost:8080')
req.add_header('Content-Type', 'application/json')




while True:
        sleep_time=getEPS()
        for x in range(0,100):
                value = random.randint(0,2);
                action = actions[value];
                event_data = {'value':value,'action':action, 'timestamp':time.time()}
		print event_data
		response = urllib2.urlopen(req, json.dumps(event_data))
#		print response
		time.sleep(sleep_time)



