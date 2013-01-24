'''
    Created on 2 Jan 2013
    @author: Mel
'''
import string, cgi, time
from os import curdir, sep
import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import sys, os
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SocketServer
import threading
import sys
import web
   
class LocalServer(threading.Thread):
    """
        Serves simple HTTP requests to the local HTML page running in the main window
    """
    host = "127.0.0.1"
    port = 8000
    app = None

    def __init__(self, host=None, port=None):
        threading.Thread.__init__(self)
        
        if host is None:
            host = "127.0.0.1"            
        self.host = host
        
        if port is None:
            port = 8000            
        self.port = port

    def run(self):        
        web.config.debug = True
        urls = (
                '/services/Symbols/GetAll', 'services.Symbols.GetAll'
                )
        self.app = web.application(urls, globals())
        print self.app
        print self.app.request
        self.app.run()
        
        #app.runsimple(server_address=('127.0.0.1', 8080))
        
def main():
    try:
        web.config.debug = True
        urls = (
                '/', 'index.html'
                '/services/Symbols/GetAll', 'services.Symbols.GetAll'
                )   
        app = web.application(urls, globals())
        print app
        print app.request
        app.run()
        
        
        
        
        """
        server = LocalServer()
        server.start()
        print "Started"
        """
        
    except KeyboardInterrupt:
        print '^C received, shutting down server'

if __name__ == '__main__':
    main()

"""
#from assetjet.util import web
    def run(self):        
        handler = web.SimpleHTTPRequestHandler
        httpd = HTTPServer((self.host, self.port), handler)
        print "Server initialised at Address:", httpd.server_address
        httpd.serve_forever()
"""
