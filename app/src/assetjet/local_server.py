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

    def __init__(self, host=None, port=None):
        threading.Thread.__init__(self)
        
        if host is None:
            host = "127.0.0.1"            
        self.host = host
        
        if port is None:
            port = 8000            
        self.port = port

    def run(self):        
        urls = (
                '/', 'index'
                )
        app = web.application(urls, globals())
        app.run()  
        print "Server initialised :"
        
def main():
    try:
        server = LocalServer()
        server.run()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

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
