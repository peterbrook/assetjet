'''
Created on 16 Jan 2013

@author: Mel
'''
import sys
"""
for item in sys.path:
    print item
"""

from assetjet.cfg import db
import sqlalchemy.orm as orm
import json

from assetjet.model import asset

def GetAll():
    Session = orm.sessionmaker(bind=db.GetEngine())        
    session = Session()
    return session.query(asset.Asset).all()

if __name__ == "__main__":
    all = GetAll()
    print "retrieved objects"
    print all