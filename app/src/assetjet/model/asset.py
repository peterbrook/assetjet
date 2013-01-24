
from sqlalchemy import Column, Integer, String
from datetime import date
import base 
from assetjet.cfg import db
from sqlalchemy.orm import sessionmaker
import json

class Asset(base.ModelBase, base.ajModel):
    __tablename__ = 'assets'

    cd = Column(String, primary_key=True)
    name = Column(String)
    gicssectorid = Column(Integer)

    def __init__(self, cd, name, gicssectorid):
        self.cd = cd
        self.name = name
        self.gicssectorid = gicssectorid
    
    def __repr__(self):
        return json.JSONEncoder().encode(self.__dict__) 
    
        #return "<Asset('%s','%s', '%s')>" % (self.cd, self.name, self.gicssectorid)
