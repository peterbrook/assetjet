from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import string,cgi,time
from os import curdir, sep
import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import sys, os
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SocketServer
import threading
import sys
   
class LocalServer(threading.Thread):
    """
        Serves simple HTTP requests to the local HTML page running in the main window
    """
    host = "127.0.0.1"
    port = 8000

    def __init__(self, host=None, port=None):
        threading.Thread.__init__(self)
        
        if host is None:
            host = "127.0.0.1"            
        self.host = host
        
        if port is None:
            port = 8000            
        self.port = port

    def run(self):        
        handler = SimpleHTTPRequestHandler
        httpd = HTTPServer((self.host, self.port), handler)
        print "Server initialised at Address:", httpd.server_address
        httpd.serve_forever()

def main():
    try:
        #server = HTTPServer(('', 80), SimpleHandler)
        server = HTTPServer(('', 80), SimpleHTTPRequestHandler)
        print 'Started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
