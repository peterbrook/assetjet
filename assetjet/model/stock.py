from sqlalchemy import Column, Integer, String
from datetime import date
import ModelBase

class StockDaily(ModelBase.Base):
    __tablename__ = 'stock'

    symbol = Column(String, primary_key=True)
    date = Column(date, primary_key=True)
    price_open = Column(float)
    price_high = Column(float)
    price_close = Column(float)
    volume = Column(Integer)
    adjclose = Column(float)

    def __init__(self, symbol, date, price_open, price_high, price_close, volume, adjclose):
        self.symbol = symbol
        self.date = date
        self.price_open = price_open
        self.price_high = price_high
        self.price_close = price_close
        self.volume = volume
        self.adjclose = adjclose

    def __repr__(self):
        return "<StockDaily('%s','%s', '%s', '%s', '%s', '%s', '%s')>" % \
        (   self.symbol, self.date, self.price_open, self.price_high, \
            self.price_close, self.volume, self.adjclose)
        
