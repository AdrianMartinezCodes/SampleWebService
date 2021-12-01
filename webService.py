import cherrypy
import myUser

user = myUser.myUser()

class MyWebService(object):        
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def input(self):
      data = cherrypy.request.json
      user.transaction(data)
      return
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def spendPoints(self):
        data = cherrypy.request.json
        return user.spendPoints(data)

    @cherrypy.expose
    def checkBalance(self):
        return user.checkBalance()
    
    @cherrypy.expose
    def shutdown(self):  
        cherrypy.engine.exit()
if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(MyWebService())

