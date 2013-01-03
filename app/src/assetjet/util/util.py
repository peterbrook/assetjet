import os, sys

"""
    Convenience function to return the root of the application in the 
    filesystem depending on the execution context. this is necessary to 
    allow the same code to run in the executable format and while 
    debugging as a script
     
"""

def getBaseDir():
    if getattr(sys,"frozen",False):
        return os.path.dirname(os.path.abspath(sys.executable))
    else:
        # Customize this to point to the directory of the main.py script.
        return "C:\\src\\GitHub\\assetjet\\app\\"
        #return os.path.dirname(os.path.abspath(sys.argv[0]))
    
    
if __name__ == "__main__":
    print sys.executable
    print sys.argv
    print getBaseDir()