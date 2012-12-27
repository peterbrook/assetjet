# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:17:40 2012

@author: Mel
"""

import logging, logging.handlers
# create logger with 'spam_application'
logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
# create file handler which logs only error messages
fh = logging.FileHandler('tripping.nemesis.errors.log.txt')
fh.setLevel(logging.ERROR)
# create file handler which logs even debug messages
dbg = logging.FileHandler('tripping.nemesis.debug.log.txt')
dbg.setLevel(logging.DEBUG)
# create console handler 
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
dbg.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
logger.addHandler(dbg)

