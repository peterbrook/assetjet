"""
Run this script to serve the files in the dist folder over http://localhost:8000
This is very handy to test out Esky locally.
"""

import SimpleHTTPServer
import SocketServer
import os

os.chdir('./dist')

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()



