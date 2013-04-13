'''
    Created on 2 Jan 2013
    @author: Mel
'''
import threading
import bottle
import assetjet.services.prices.getByTicker

class LocalServer(threading.Thread):
    """
        Serves simple HTTP requests to the local HTML page running in the main window
    """
    def __init__(self, host=None, port=None):
        threading.Thread.__init__(self)

    def run(self):
        bottle.run(host='localhost', port=2000)
        
def main():
    try:
        server = LocalServer()
        server.run()
    except KeyboardInterrupt:
        print '^C received, shutting down server'

if __name__ == '__main__':
    main()
