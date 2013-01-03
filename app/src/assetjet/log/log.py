# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:17:40 2012

@author: Mel
"""

import logging, logging.handlers, os
from assetjet.util import util

__logDir = 'logfiles'
__logFile = 'assetjet'

def getLogFileName(logLevel):
    return os.path.join(util.getBaseDir(), __logDir, __logFile + '.' + logLevel + '.log.txt')

# create ____loggerwith 'spam_application'
__logger= logging.getLogger('')
__logger.setLevel(logging.DEBUG)

# create file handler whi__ch logs only error messages
__fh = logging.FileHandler(getLogFileName(logLevel='error'))
__fh.setLevel(logging.ERROR)

# create file handler whi__ch logs even debug messages
__dbg = logging.FileHandler(getLogFileName('debug'))
__dbg.setLevel(logging.DEBUG)

# create console handler 
__ch = logging.StreamHandler()
__ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
__formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
__fh.setFormatter(__formatter)
__ch.setFormatter(__formatter)
__dbg.setFormatter(__formatter)

# add the handlers to the __logger
__logger.addHandler(__fh)
__logger.addHandler(__ch)
__logger.addHandler(__dbg)

def Error(msg, *args, **kwargs):
    __logger.error(msg.format(args, kwargs))

def Debug(msg, *args, **kwargs):
    __logger.debug(msg.format(args, kwargs))

def Info(msg, *args, **kwargs):
    __logger.info(msg.format(args, kwargs))
    
def Warn(msg, *args, **kwargs):
    __logger.warn(msg.format(args, kwargs))
    
    