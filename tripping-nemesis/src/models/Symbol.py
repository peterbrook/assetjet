from sqlalchemy import Column, Integer, String
from datetime import date
import ModelBase

class Symbol(ModelBase.Base):
    __tablename__ = 'symbol'

    symbol = Column(String, primary_key=True)
    startdate = Column(date)
    enddate = Column(date)
    entries = Column(Integer)

    def __init__(self, symbol, startdate, enddate, entries):
        self.symbol = symbol
        self.startdate = startdate
        self.enddate = enddate
        self.entries = entries
        
    def __repr__(self):
        return "<Symbol('%s','%s', '%s', '%s')>" % (self.symbol, self.startdate, self.enddate, self.entries)