'''
Created on 2 Jan 2013

@author: Mel
'''
from subprocess import call
from publish import dev

# Freeze it and produce patches in case older versions are in the directory
def main():
    #call('python setup_esky.py bdist_esky_patch')
    dev.publish()
    
if __name__ == '__main__':
    main()
    
    