from pandas import DataFrame
import pandas as pd
import sqlite3
import numpy as np
from datetime import date, datetime
from assetjet.cfg import db
from assetjet.log import log
import sqlalchemy.orm as orm
import json
import assetjet.model
from assetjet.model import asset
from datetime import datetime
from datetime import time
from urllib2 import *
import numpy as np
import dateutil.parser
from assetjet.util import util
import bottle

@bottle.route('/services/Prices/GetByTicker/')
def index():
    ticker = bottle.request.GET.get('ticker')
    startDate = dateutil.parser.parse(bottle.request.GET.get('startDate'))
    endDate = dateutil.parser.parse(bottle.request.GET.get('endDate'))
    period = bottle.request.GET.get('period')
    closePrices, seriesbegin = getAdjClosePrices([ ticker ], startDate, endDate)
    pricesRebased = getPricesRebased(closePrices, seriesbegin, base=100, asjson=True)
    return "_jqjsp(" + pricesRebased  + ");"

def getPricesRebased(prices, startdates, base=100, asjson=False, frequency=None):

    """ Returns a pandas dataframe (in json format if asjson=True) with prices
        rebased to base, optionally with a new frequency:
        e.g. 'D','M', 'W-FRI' for daily, end of month or friday-weekly data
    """
    # Returns    
    returns = prices.pct_change()
    # Rebasing
    pricesRebased = (1 + returns).cumprod()
    # requires NumPy 1.7 !! (1.6 doesn't translate datetime correctly)
    for col in pricesRebased:
        pricesRebased.ix[startdates.ix[col,0],col] = 1 
    pricesRebased = pricesRebased * base
    if frequency:
        pricesRebased = pricesRebased.asfreq(frequency, method='ffill')    
    if asjson:
        # dataframe to_json() method is still pending, therefore:
        return tojson(pricesRebased.reset_index())
        
    else:
        return pricesRebased 
    
def tojson(df):
    """
    convert a pandas data frame into a JSON object
    """     
    d = [ 
        dict([(colname, row[i]) for i, colname in enumerate(df.columns)])
        for row in df.values
    ]
    # json cannot deal with datetime objects, therefore convert into string
    dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime) else None
    
    ret = json.dumps(d, default=dthandler, indent=4)
#    print ret # must be disabled for freezing
    return ret
    #return json.dumps(d, indent=4)

def getAdjClosePrices(tickers, startdate, enddate):
    """ returns a ready to use pandas DataFrame and a Series with the startDate
    """
    Session = orm.sessionmaker(bind=db.GetEngine())        
    session = Session()
    conn = db.GetEngine().connect()
    # Query
    conn.execute("""CREATE TEMP TABLE Tickers (Cd Text)""")
    conn.execute("""INSERT INTO Tickers VALUES(?)""", zip(tickers))
    
    result = conn.execute("""SELECT ts.Cd, Date, AdjClose
                      FROM TimeSeries ts
                      INNER JOIN Tickers t ON ts.Cd = t.Cd
                      WHERE ts.Date >= ? AND ts.Date <= ?""", (startdate, enddate))
    rows = result.fetchall()

    # Create a pandas DataFrame
    pricesRaw = DataFrame.from_records(rows, columns=['Cd', 'Date', 'AdjClose'])
    # Convert Date strings into datetime so pandas can do time series stuff
    pricesRaw.Date = pd.to_datetime(pricesRaw.Date)
    seriesbegin = pricesRaw[['Cd','Date']].groupby('Cd').min()
    # Pivot DataFrame
    prices = pricesRaw.pivot(index='Date', columns='Cd', values='AdjClose')

    # Close DB and Cursor
    conn.close()
    return prices, seriesbegin
    
if __name__ == "__main__":
    tickers = [ 'AAPL','MMM', 'ACE', 'ABT', 'ANF', 'ACN', 'ADBE', 'ADT', 'AMD', 'AES', 'AET' ]
    startdate = '2011-01-01'
    enddate = date.today()
    
    # Get rebased prices
    closePrices, seriesbegin = getAdjClosePrices(tickers, startdate, enddate)
    pricesRebased = getPricesRebased(closePrices, seriesbegin, base=100, asjson=False, frequency='M')
#    print pricesRebased
