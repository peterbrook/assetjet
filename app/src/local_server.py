'''
    Created on 2 Jan 2013
    @author: Mel
'''
import threading
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response
from assetjet.log import log
from assetjet.services.Prices import GetByTicker

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
        try:
            config = Configurator()
            config.add_route('services.Symbols.GetAll', \
                             'services/Symbols/GetAll/')
            
            config.add_route('services.Prices.GetByTicker', \
                             'services/Prices/GetByTicker/')
                
            config.scan('assetjet.services')
            app = config.make_wsgi_app()
            server = make_server(self.host, self.port, app)
            log.Debug("Serving on :", self.host, self.port)
            server.serve_forever()
        except Exception:
            log.Error(Exception.message)

        config = Configurator()
        config.add_route('services.Symbols.GetAll', 'services/Symbols/GetAll/')     
        config.add_route('services.Prices.GetByTicker', 'services/Prices/GetByTicker/')
            
        try:
#            config.scan('assetjet.services') # not found by frozen version
            config.scan()
        except Exception, e:
            log.Debug(str(e))
            
        app = config.make_wsgi_app()
        
        # Logging the server activity under assetjet.debug.log.txt
        from paste.translogger import TransLogger
        app = TransLogger(app, setup_console_handler=False)
        
        server = make_server(self.host, self.port, app)
        log.Debug("Serving on: {0}, {1}".format(self.host, self.port))
        
        server.serve_forever()

# Workaround: the frozen version can't handle config.scan(assetjet.services) properly
@view_config(route_name="services.Prices.GetByTicker")   
def GET(request):
    return GetByTicker.GET(request)               
        
def main():
    try:
        server = LocalServer()
        server.run()
    except KeyboardInterrupt:
        print '^C received, shutting down server'

if __name__ == '__main__':
    main()
