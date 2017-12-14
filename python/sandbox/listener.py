import random
import string
import json
import cherrypy
import mysql.connector
from cherrypy.process import wspbus
import copy
from threading import Lock

config = {
  'user': 'denver',
  'password': 'Admin123',
  'host': '127.0.0.1',
  'database': 'trafficData',
  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
add_event = ("INSERT INTO events "
               "(ts, value, Action) "
               "VALUES (FROM_UNIXTIME(%(timestamp)s), %(value)s, %(action)s)")

mutex = Lock()

def initDBConnection():
	print "DB connection setup"

def insertEventToDB(requestBody):
	try :
		data = json.loads(requestBody.read())
		action = data.get("action")
		value = int(data.get("value"))
		timestamp = float(data.get("timestamp"))
		eventData = {'value':value, 'action':action, 'timestamp':timestamp} 
		cursor.execute(add_event, eventData)
		cnx.commit()
#		print "inserted data into DB with timestamp"  
		print eventData.get("timestamp")
	except Exception as inst:
		print inst


@cherrypy.expose
class StringGeneratorWebService(object):

    @cherrypy.tools.accept(media='text/plain')

    def POST(self, length=8):
	mutex.acquire()
	insertEventToDB(cherrypy.request.body)
	mutex.release()

if __name__ == '__main__':
	initDBConnection()	

	cherrypy.engine.subscribe("eventBus", insertEventToDB)
	i = 1 
	conf = {
		'/': {
		'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            	'tools.sessions.on': True,
            	'tools.response_headers.on': True,
            	'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        	}
	}
	cherrypy.quickstart(StringGeneratorWebService(), '/', conf)
