'''
Created on 28 Dec 2012

@author: Mel
'''

import unittest, os, sys
import store
import model

def getAllModels():
    testdir = os.curdir
    print ("testdir", testdir)


class StoreTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    
    def testGetAll(self):
        getAllModels()
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()