"""
Run this script to create the TimeSeries.db sample database with all S&P500
tickers as downloaded from Wikipedia and daily time series 
"""

import os
import sqlite3
from lxml import html
import database

def download_sp500(startdate, enddate, dbfilename):
    
    # Download list of tickers, company name and GICS Sectors from Wikipedia
    # TODO: somebody please improve this
    url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    page = html.parse(url)
    symbol = page.xpath('//table[@class="wikitable sortable"]/tr/td[1]/a/text()')
    company = page.xpath('//table[@class="wikitable sortable"]/tr/td[2]/a/text()')
    sector = page.xpath('//table[@class="wikitable sortable"]/tr/td[4]/text()')
    
    # Since Dec-12, BRK.B Yahoo! Finance lists BRK.B as BRK-B
    if 'BRK.B' in symbol: symbol[symbol.index('BRK.B')]='BRK-B'
    
    # If database doesn't exist, create it
    if not os.path.exists(dbfilename):
        database.create_db(dbfilename)    
    
    conn = sqlite3.connect(dbfilename, 
           detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    
    # Load data from Wikipedia into Load table
    conn.execute("CREATE TABLE LoadAssets (Cd text, Name text, SectorName text)")
    sql = "INSERT INTO LoadAssets (Cd, Name, SectorName) VALUES (?, ?, ?)"    
    c.executemany(sql, zip(symbol, company, sector))
    conn.commit()
    
    database.populate_db(symbol, startdate, enddate, dbfilename)
    
    # TODO: download with lxml (?)
    # http://en.wikipedia.org/wiki/Global_Industry_Classification_Standard
    # Note: Telecommunication Services is listed as Telecommunications Services
    conn.execute("DELETE FROM GicsSectors")
    conn.execute("INSERT INTO GicsSectors VALUES(10, 'Energy')")
    conn.execute("INSERT INTO GicsSectors VALUES(15, 'Materials')")
    conn.execute("INSERT INTO GicsSectors VALUES(20, 'Industrials')")
    conn.execute("INSERT INTO GicsSectors VALUES(25, 'Consumer Discretionary')")
    conn.execute("INSERT INTO GicsSectors VALUES(30, 'Consumer Staples')")
    conn.execute("INSERT INTO GicsSectors VALUES(35, 'Health Care')")
    conn.execute("INSERT INTO GicsSectors VALUES(40, 'Financials')")
    conn.execute("INSERT INTO GicsSectors VALUES(45, 'Information Technology')")
    conn.execute("INSERT INTO GicsSectors VALUES(50, 'Telecommunications Services')")
    conn.execute("INSERT INTO GicsSectors VALUES(55, 'Utilities')")
    
    conn.execute("DELETE FROM Assets WHERE Cd IN (SELECT Cd FROM LoadAssets)")
    
    conn.execute("""
    INSERT INTO Assets
    SELECT l.Cd, l.Name, g.Id
    FROM LoadAssets l
    INNER JOIN GicsSectors g ON l.SectorName = g.Name""")
    
    conn.execute("DELETE FROM Indices WHERE Cd = '^GSPC' ")
    conn.execute("INSERT INTO Indices VALUES('^GSPC', 'S&P 500')")
    
    conn.execute("DELETE FROM AssetsIndices WHERE IndexCd = '^GSPC' ")
    conn.execute("INSERT INTO AssetsIndices SELECT Cd, '^GSPC' FROM LoadAssets")
    
    conn.execute("DROP TABLE LoadAssets")
    conn.commit()
   
    c.close()
    conn.close()

# Create/Update sample database with S&P 500    
if __name__ == '__main__': 
   download_sp500('2012-1-1', '2012-12-12', 'TimeSeries.db')
