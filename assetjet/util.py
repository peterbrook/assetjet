import os, sys

def getbasedir():
    if getattr(sys,"frozen",False):
        return os.path.dirname(os.path.abspath(sys.executable))
    else:
        return os.path.dirname(os.path.abspath(sys.argv[0]))