import random
import string
import json
import cherrypy

def initDBConnection:
	print "DB connection setup"

def insertEventToDB(eventData):
	print "inserted data into DB with timestamp"

@cherrypy.expose
class StringGeneratorWebService(object):

    @cherrypy.tools.accept(media='text/plain')

    def POST(self, length=8):
	data = json.loads(cherrypy.request.body.read())
	print data.get("receiver")



if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.quickstart(StringGeneratorWebService(), '/', conf)
