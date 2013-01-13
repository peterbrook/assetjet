'''
Created on 2 Jan 2013

@author: Mel
'''
import sys, os
import SimpleHTTPServer
import SocketServer
import threading
from assetjet.cfg import cfg    
   
class LocalServer(threading.Thread):
    """
        Serves simple HTTP requests to the local HTML page running in the main window
    """
    url = ""
    automatic = True

    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):        
        PORT = 8000
        handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer((self.url, PORT), handler)
        print "serving at port", PORT
        print "Server Address:", httpd.server_address
        httpd.serve_forever()
               
