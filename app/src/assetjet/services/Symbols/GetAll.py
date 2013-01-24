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
import web

import assetjet.model

from assetjet.model import asset

class GetAll:
    
    def GET(self):
        Session = orm.sessionmaker(bind=db.GetEngine())        
        session = Session()
        assets = session.query(asset.Asset).all()
        dict = {}
        for aItem in assets:
            dict[aItem.cd] = (aItem.cd, aItem.name, aItem.gicssectorid)        
        return json.dumps(dict)
    
if __name__ == "__main__":
    all = GetAll().GET()
    print "retrieved objects"
    print all