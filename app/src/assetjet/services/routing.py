'''
Created on 25 Jan 2013

@author: Mel
'''
from pyramid.config import Configurator

def ServiceRouting(config):
    config.add_route('symbols.GetAll', '/symbols/GetAll/')