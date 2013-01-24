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
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import assetjet.services
from assetjet.services import Symbols


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
        host = '127.0.0.1'
        port = 80
        config = Configurator()
        config.add_route('symbols.GetAll', '/symbols/GetAll/{name}')
        config.add_view(Symbols.GetAll, route_name='symbols.GetAll')
        app = config.make_wsgi_app()
        server = make_server(host, port, app)
        print ("Serving on:", host, port)
        server.serve_forever()
        
def main():
    try:
        server = LocalServer()
        server.run()
    except KeyboardInterrupt:
        print '^C received, shutting down server'

if __name__ == '__main__':
    main()
