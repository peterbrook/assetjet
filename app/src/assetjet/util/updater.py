'''
Created on 2 Jan 2013

@author: Mel
'''
import sys, os
import esky
import threading
from assetjet.cfg import cfg    
   
class Updater(threading.Thread):
    '''
        This class encapsulates multi-threaded logic for updating the application using Esky
    '''
    url = ""
    automatic = True

    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        
    def run(self):        
        if getattr(sys,"frozen",False):
            try:        
                frozenapp = esky.Esky(sys.executable, self.url)
                new_version = frozenapp.find_update()
                if(new_version != None):
                    #frozenapp.fetch_version(version=new_version, callback=)
                    frozenapp.auto_update()
                    appexe = esky.util.appexe_from_executable(sys.executable)
                    os.execv(appexe,[appexe] + sys.argv[1:])
            except Exception, e:
                print "ERROR UPDATING APP:", e
            frozenapp.cleanup()   
               
