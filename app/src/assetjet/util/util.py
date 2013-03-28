import os, sys, inspect
import urllib2


def getBaseDir():
    """
    Convenience function to return the path to main.py depending on the
    execution context. this is necessary to allow the same code to run 
    in the executable format and while debugging as a script.
    """
    if getattr(sys,"frozen",False):
        # If this is running in the context of a frozen (executable) file, 
        # we return the path of the main application executable
        return os.path.dirname(os.path.abspath(sys.executable))
    else:
        # If we are running in script or debug mode, we need 
        # to inspect the currently executing frame. This enable us to always
        # derive the directory of main.py no matter from where this function
        # is being called
        thisdir = os.path.dirname(inspect.getfile(inspect.currentframe()))
        return os.path.abspath(os.path.join(thisdir, '..', '..'))


def test_url(url):
    """
    Check if an internet connection can be established
    """
    try:
        response=urllib2.urlopen(url,timeout=2)
        return True
    except urllib2.URLError as err: pass
    return False