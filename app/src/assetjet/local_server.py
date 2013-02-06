'''
    Created on 2 Jan 2013
    @author: Mel
'''
import sys
sys.path.append('..')
sys.path.append('.')
import threading
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

#from services import Symbols
import services.Symbols.GetAll

#from services import routing
#from services.Symbols import GetAll


class LocalServer(threading.Thread):
    """
        Serves simple HTTP requests to the local HTML page running in the main window
    """
    host = "127.0.0.1"
    port = 80
    app = None

    def __init__(self, host=None, port=None):
        threading.Thread.__init__(self)
        
        if host is None:
            host = "127.0.0.1"            
        self.host = host
        
        if port is None:
            port = 8080
        self.port = port

    def run(self):
        config = Configurator()
        config.add_route('services.Symbols.GetAll', \
                         'services/Symbols/GetAll/')
        
        config.add_route('services.Prices.GetByTicker', \
                         'services/Prices/GetByTicker/')
            
        config.scan('services')
        app = config.make_wsgi_app()
        server = make_server(self.host, self.port, app)
        print ("Serving on :", self.host, self.port)
        server.serve_forever()
        
def main():
    try:
        server = LocalServer()
        server.run()
    except KeyboardInterrupt:
        print '^C received, shutting down server'

if __name__ == '__main__':
    main()
