# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 06:24:49 2012

@author: Mel
"""
import os
from sqlalchemy import create_engine
import ConfigParser
from assetjet.util import getbasedir

# the config file is stored in the parent directory of either 
# main.py in development or the executable when frozen
cfg_loc = os.path.dirname(getbasedir())

config = ConfigParser.SafeConfigParser()
config.read(os.path.join(cfg_loc,'app.cfg'))

if not config.has_section('Database'):
    # TODO: Ask for user input instead of default path here
    config.add_section('Database')
    config.set('Database', 'filepath', r'C:\assetjet.db')
    with open(os.path.join(cfg_loc,'app.cfg'), 'wb') as configfile:
        config.write(configfile)
defaultDbFileName = str(config.get('Database', 'filepath'))
filePath = defaultDbFileName

def GetEngine():
    connString = "sqlite:///{0}".format(filePath)
    print connString
    return create_engine(connString)
    