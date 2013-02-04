'''
Created on 16 Jan 2013

@author: Mel
'''
import sys
#sys.path.append('..')

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
from pyramid.view import view_config
from pyramid.response import Response


#@view_config(route_name="services/Symbols/GetAll/", renderer="json")
@view_config(route_name="services/Symbols/GetAll/")
def GET(request):
    Session = orm.sessionmaker(bind=db.GetEngine())        
    session = Session()
    assets = session.query(asset.Asset).all()
    dict = {}
    dict['success'] = True
    assetsList = []
    for aItem in assets:
        assetsList.append({'SymbolCode': aItem.cd, 'SymbolName': aItem.name, 'SymbolGisSector': aItem.gicssectorid})
    dict['assets'] = assetsList

    strResp = json.dumps(dict)
    return Response(str("onJsonpCallback(" + strResp  + ");"))
    
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
    