import mysql.connector
import time
import random
import string
import configparser
from mysql.connector import errorcode
from datetime import date, datetime, timedelta


def getEPS():
	config = configparser.ConfigParser()
	config.read('events.ini')
	eps = float(config['DEFAULT']['events_per_sec'])
	sleep_time = 1.0/eps
	return sleep_time

config = {
  'user': 'denver',
  'password': 'Admin123',
  'host': '127.0.0.1',
  'database': 'trafficData',
  'raise_on_warnings': True,
}


cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

DB_NAME = 'trafficData'


add_event = ("INSERT INTO events "
               "(ts, value, Action) "
               "VALUES (CURRENT_TIMESTAMP, %(value)s, %(action)s)")

actions = ("BLOCK","ALLOW","TRUST");

while True:
	sleep_time=getEPS()
	for x in range(0,100):
		value = random.randint(0,0);
		action = actions[value];
		event_data = {'value':value,'action':action}
		cursor.execute(add_event, event_data)
		print(event_data)
		time.sleep(sleep_time)
		cnx.commit()




cursor.close()
cnx.close()

