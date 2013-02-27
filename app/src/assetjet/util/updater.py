'''
Created on 2 Jan 2013

@author: Mel
'''
import sys, os
import esky
import threading
from assetjet.cfg import cfg
from assetjet.log import log  

# Disabled threading for now as at the moment, it would suddenly leave the app
# to restart

#class Updater(threading.Thread):
class Updater():
    '''
        This class encapsulates multi-threaded logic for updating the application using Esky
    '''
    url = ""
    automatic = True

    def __init__(self, url):
#        threading.Thread.__init__(self)
        self.url = url
        
    def run(self):        
        if getattr(sys,"frozen",False):
            try:
                log.Debug('Checking for new version at {0}'.format(self.url))
                frozenapp = esky.Esky(sys.executable, self.url)
                new_version = frozenapp.find_update()
                if new_version:
                    log.Debug('Found new version: {0}'.format(new_version))
                else:
                    log.Debug('No new version found')
                if(new_version != None):
                    #frozenapp.fetch_version(version=new_version, callback=)
                    frozenapp.auto_update()
                    appexe = esky.util.appexe_from_executable(sys.executable)
                    os.execv(appexe,[appexe] + sys.argv[1:])
            except Exception, e:
                log.Error("Error updating app:", e)
            frozenapp.cleanup()   
               
