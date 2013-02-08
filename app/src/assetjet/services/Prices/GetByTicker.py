'''
Created on 5 Feb 2013

@author: Mel
'''

from pandas import DataFrame
import pandas as pd
import sqlite3
import numpy as np
from datetime import date, datetime
from assetjet.cfg import db
import sqlalchemy.orm as orm
#import simplejson as json
import json
import web
import assetjet.model
from assetjet.model import asset
from pyramid.view import view_config
from pyramid.response import Response
from datetime import datetime
from datetime import time
from urllib2 import *
import numpy as np
import dateutil.parser

#@view_config(route_name="services/Symbols/GetAll/", renderer="json")
@view_config(route_name="services.Prices.GetByTicker")
def GET(request):
    ticker = request.params['ticker']
    startDate = dateutil.parser.parse(request.params['startDate'])
    endDate = dateutil.parser.parse(request.params['endDate'])
    period = request.params['period']
    callbackParam = "_jqjsp"
    
    print (ticker, startDate, endDate, period)
    
    closePrices, seriesbegin = getAdjClosePrices([ ticker ], startDate, endDate)
    pricesRebased = getPricesRebased(closePrices, seriesbegin, base=100, asjson=True)
    return Response(str("_jqjsp(" + pricesRebased  + ");"))

def get_yahoo_prices(symbol, startdate=None, enddate=None,
                     period='d', datefmt="%Y-%m-%d"):
    
    """ Utility function to pull price data from Yahoo Finance site.
    
        Parameters:
        symbol: string, a valid financial instrument symbol
        startdate: string, a date string representing the beginning date
            for the requested data.
        enddate: string, a date string representing the ending date for the 
            requested data.
        period: string {'d', 'w', 'y'}, representing the period of data
            requested.
        datefmt: string, a date format string designating the format for
            the startdate and enddate input parameters.
        
        Returns:
        numpy array containing dates and price/volume data in the following
        dtype:
        numpy.dtype({'names':['symbol', 'date', 'open', 'high', 'low',
                              'close', 'volume', 'adjclose'],
                     'formats':['S8', 'M8[D]', float, float, float, float,
                                float, float]})
    """
    
    todaydate = datetime.date(*time.localtime()[:3])
    yesterdate = todaydate - datetime.timedelta(1)
    lastyeardate = todaydate - datetime.timedelta(365)
    
    if startdate is None:
        startdate = lastyeardate
    else:
        startdate = datetime.datetime.strptime(startdate, datefmt)
    
    if enddate is None:
        enddate = yesterdate
    else:
        enddate = datetime.datetime.strptime(enddate, datefmt)
    
    # Note: account for Yahoo's messed up 0-indexed months
    url = "http://ichart.finance.yahoo.com/table.csv?s=%s&a=%d&b=%d&c=%d&"\
              "d=%d&e=%d&f=%d&y=0&g=%s&ignore=.csv" % (symbol,
              startdate.month-1, startdate.day, startdate.year,
              enddate.month-1, enddate.day, enddate.year, period)
    
    filehandle = urlopen(url)
    lines = filehandle.readlines()
    
    data = []
    
    for line in lines[1:]:
        items = line.strip().split(',')
        if len(items)!=7:
            # skip bad data for now
            continue
        
        dt = items[0]
        opn, high, low, close, volume, adjclose = [float(x) for x in items[1:7]]
        data.append((symbol, dt, opn, high, low, close, volume, adjclose))
    
    npdata = np.array(data, dtype=schema)
    
    return npdata

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
        dict([
            (colname, row[i]) 
            for i,colname in enumerate(df.columns)
        ])
        for row in df.values
    ]
    
    # json cannot deal with datetime objects, therefore convert into string
    dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime) else obj
    
    return json.dumps(d, default=dthandler, indent=4)

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
    tickers = ['AAPL','MMM', 'ACE', 'ABT', 'ANF', 'ACN', 'ADBE', 'ADT', 'AMD', 'AES', 'AET']
    startdate = '2011-01-01'
    enddate = date.today()
    
    # Get rebased prices
    closePrices, seriesbegin = getAdjClosePrices(tickers, startdate, enddate)
    pricesRebased = getPricesRebased(closePrices, seriesbegin, base=100, asjson=False, frequency='M')
#    print pricesRebased

