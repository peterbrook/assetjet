
from sqlalchemy import Column, Integer, String
from datetime import date
from base import ModelBase
from src.cfg import db
from sqlalchemy.orm import sessionmaker

class Asset(ModelBase):
    __tablename__ = 'assets'

    cd = Column(String, primary_key=True)
    name = Column(String)
    gicssectorid = Column(Integer)

    def __init__(self, cd, name, gicssectorid):
        self.cd = cd
        self.name = name
        self.gicssectorid = gicssectorid
    
    def __repr__(self):
        return "<Symbol('%s','%s', '%s', '%s')>" % (self.cd, self.name, self.gicssectorid)
