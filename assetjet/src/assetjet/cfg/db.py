# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 06:24:49 2012

@author: Mel
"""
from sqlalchemy import create_engine

from assetjet.cfg import cfg

__filePath = None

def __init__():
    __filePath = cfg.root.DbFileName
    
def GetEngine():
    connString = "sqlite:///{0}".format(__filePath)
    return create_engine(connString)


if __name__ == "__main__":
    __init__()



    