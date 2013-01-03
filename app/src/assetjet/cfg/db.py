# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 06:24:49 2012

@author: Mel
"""
from sqlalchemy import create_engine
import sys, os

from assetjet.cfg import cfg
from assetjet.util import util

cfg.root.DbFileName
    
def GetEngine():
    if os.path.isfile(cfg.root.DbFileName):
        connString = "sqlite:///{0}".format(cfg.root.DbFileName)
        return create_engine(connString)
    else:
        raise Exception("File {0} does not exist", cfg.root.DbFileName)


    