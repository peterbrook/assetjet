'''
Created on 16 Jan 2013

@author: Mel
'''
from assetjet.cfg import db
from assetjet.log import log
from assetjet.util import util
from assetjet import local_server
import sqlalchemy.orm as orm

from assetjet.model import asset

def GetAll():
    Session = orm.sessionmaker(bind=db.GetEngine())        
    session = Session()
    return session.query(asset.Asset).all()