'''
Created on 2 Jan 2013

@author: Mel
'''
import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import sys, os
import SimpleHTTPServer
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SocketServer
import threading
   
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
        handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = HTTPServer((self.host, self.port), handler)
        print "Server initialised at Address:", httpd.server_address
        httpd.serve_forever()
              
"""
if __name__ == "__main__":
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = HTTPServer(("127.0.0.1", 8000), handler)
    print "Server initialised at Address:", httpd.server_address
    httpd.serve_forever()
"""

class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            print self.path
            print curdir
            print sep
            
            if self.path.endswith(".html"):
                fileToOpen = curdir + 'web' + sep + self.path
                print fileToOpen
                f = open(fileToOpen) #self.path has /test.html
                #note that this potentially makes every file on your computer readable by the internet

                self.send_response(200)
                self.send_header('Content-type',    'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            if self.path.endswith(".asj"):   # the idea is this corresponds to an assetjet service hosted locally
                self.send_response(200)
                self.send_header('Content-type',    'text/html')
                self.end_headers()
                self.wfile.write("hey, hello from AssetJet" + str(time.localtime()[7]))
                return
                
            return
                
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
     

    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            
            self.end_headers()
            upfilecontent = query.get('upfile')
            print "filecontent", upfilecontent[0]
            self.wfile.write("<HTML>POST OK.<BR><BR>");
            self.wfile.write(upfilecontent[0]);
            
        except :
            pass

def main():
    try:
        #server = HTTPServer(('', 80), SimpleHandler)
        server = HTTPServer(('', 80), SimpleHTTPServer.SimpleHTTPRequestHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()

