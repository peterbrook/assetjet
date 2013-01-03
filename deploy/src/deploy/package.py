'''
Created on 2 Jan 2013

@author: Mel
'''

AppName = "AssetJet"
Major = 0
Minor = 1
Sub = 6
Platform = "Win64"

def GetDescriptorString():
    return "{0}.{1}.{2}.{3}".format(AppName, Major, Minor, Sub)

def GetVersionString():
    return "{0}.{1}.{2}".format(Major, Minor, Sub)

class Package:
    AppName = "AssetJet"
    Major = 0
    Minor = 1
    Sub = 6
    Platform = "Win64"


    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        