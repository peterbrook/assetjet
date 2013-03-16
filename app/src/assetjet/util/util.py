import os, sys, inspect
"""
    Convenience function to return the root of the application in the 
    filesystem depending on the execution context. this is necessary to 
    allow the same code to run in the executable format and while 
    debugging as a script
     
"""

def getBaseDir():
    if getattr(sys,"frozen",False):
        # If this is running in the context of a frozen (executable) file, 
        # We use the currently executing path
        return os.path.dirname(os.path.abspath(sys.executable))
    else:
        # If we are running in script or debug mode, we need 
        # to inspect the currently executing frame to ensure that 
        # we return the path relative to the application root and not the last run script
        thisdir = os.path.dirname(inspect.getfile(inspect.currentframe()))
        #return os.path.realpath(os.path.join(thisdir, '..', '..'))
        return os.path.realpath(os.path.join(thisdir))
