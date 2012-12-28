# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 06:24:49 2012

@author: Mel
"""
from sqlalchemy import create_engine
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open('app.cfg'))
defaultDbFileName = str(config.get('Database', 'filePath'))
FilePath = defaultDbFileName

def GetEngine():
    connString = "sqlite:///{0}".format(FilePath)
    print connString
    return create_engine(connString)
    