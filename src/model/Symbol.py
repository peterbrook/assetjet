
from sqlalchemy import Column, Integer, String
from datetime import date
from base import ModelBase
from cfg import DB
from sqlalchemy.orm import sessionmaker

class Symbol(ModelBase):
    __tablename__ = 'symbol_list'

    symbol = Column(String, primary_key=True)
    startdate = Column(String)
    enddate = Column(String)
    entries = Column(Integer)

    def __init__(self):
        super(ModelBase, self)
        """
            def __init__(self, symbol, startdate, enddate, entries):
                super(ModelBase.Base, self)
                self.symbol = symbol
                self.startdate = startdate
                self.enddate = enddate
                self.entries = entries
        """
    
    def __repr__(self):
        return "<Symbol('%s','%s', '%s', '%s')>" % (self.symbol, self.startdate, self.enddate, self.entries)
