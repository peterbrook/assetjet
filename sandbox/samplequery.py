from pandas import DataFrame
import pandas as pd
import sqlite3
import numpy as np
from datetime import date, datetime
import json as json

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
    dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime) else None
    return json.dumps(d, default=dthandler, indent=4)

def getAdjClosePrices(tickers, startdate, enddate):
    """ returns a ready to use pandas DataFrame and a Series with the startDate
    """
    # Open DB Connection, TODO: switch to SQLAlchemy 
    db = '/Users/Felix/assetjet.db'
    conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()    
    
    # Query
    cursor.execute("""CREATE TEMP TABLE Tickers (Cd Text)""")
    cursor.executemany("""INSERT INTO Tickers VALUES(?)""", zip(tickers))
    
    cursor.execute("""SELECT ts.Cd, Date, AdjClose
                      FROM TimeSeries ts
                      INNER JOIN Tickers t ON ts.Cd = t.Cd
                      WHERE Date >= ? AND Date <= ?""", (startdate, enddate))
    rows = cursor.fetchall()
    
    # Create a pandas DataFrame
    pricesRaw = DataFrame(rows, columns=zip(*cursor.description)[0])
    pricesRaw.Date = pd.to_datetime(pricesRaw.Date) # convert date to datetime
    seriesbegin = pricesRaw[['Cd','Date']].groupby('Cd').min()
    # Pivot DataFrame
    prices = pricesRaw.pivot('Date', 'Cd', 'AdjClose')

    # Close DB and Cursor
    cursor.close()
    conn.close()
    return prices, seriesbegin

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
        pricesRebased.ix[seriesbegin.ix[col,0],col] = 1 
    pricesRebased = pricesRebased * base
    if frequency:
        pricesRebased = pricesRebased.asfreq(frequency, method='ffill')    
    if asjson:
        # dataframe to_json() method is still pending, therefore:
        return tojson(pricesRebased.reset_index())
    else:        
        return pricesRebased 
    

if __name__ == '__main__':
    # Parameters
    tickersAll = ['MMM', 'ACE', 'ABT', 'ANF', 'ACN', 'ADBE', 'ADT', 'AMD', 'AES', 'AET', 'AFL', 'A', 'GAS', 'APD', 'ARG', 'AKAM', 'AA', 'ALXN', 'ATI', 'AGN', 'ALL', 'ALTR', 'MO', 'AMZN', 'AEE', 'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AMGN', 'APH', 'APC', 'ADI', 'AON', 'APA', 'AIV', 'APOL', 'AAPL', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP', 'AN', 'AZO', 'AVB', 'AVY', 'AVP', 'BHI', 'BLL', 'BAC', 'BK', 'BCR', 'BAX', 'BBT', 'BEAM', 'BDX', 'BBBY', 'BMS', 'BRK-B', 'BBY', 'BIG', 'BIIB', 'BLK', 'HRB', 'BMC', 'BA', 'BWA', 'BXP', 'BSX', 'BMY', 'BRCM', 'BF.B', 'CHRW', 'CA', 'CVC', 'COG', 'CAM', 'CPB', 'COF', 'CAH', 'CFN', 'KMX', 'CCL', 'CAT', 'CBG', 'CBS', 'CELG', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHK', 'CVX', 'CMG', 'CB', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CTXS', 'CLF', 'CLX', 'CME', 'CMS', 'COH', 'KO', 'CCE', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CSC', 'CAG', 'COP', 'CNX', 'ED', 'STZ', 'CBE', 'GLW', 'COST', 'CVH', 'COV', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DF', 'DE', 'DELL', 'DNR', 'XRAY', 'DVN', 'DO', 'DTV', 'DFS', 'DISCA', 'DLTR', 'D', 'RRD', 'DOV', 'DOW', 'DPS', 'DTE', 'DD', 'DUK', 'DNB', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMC', 'EMR', 'ESV', 'ETR', 'EOG', 'EQT', 'EFX', 'EQR', 'EL', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'XOM', 'FFIV', 'FDO', 'FAST', 'FII', 'FDX', 'FIS', 'FITB', 'FHN', 'FSLR', 'FE', 'FISV', 'FLIR', 'FLS', 'FLR', 'FMC', 'FTI', 'F', 'FRX', 'FOSL', 'BEN', 'FCX', 'FTR', 'GME', 'GCI', 'GPS', 'GD', 'GE', 'GIS', 'GPC', 'GNW', 'GILD', 'GS', 'GT', 'GOOG', 'GWW', 'HAL', 'HOG', 'HAR', 'HRS', 'HIG', 'HAS', 'HCP', 'HCN', 'HNZ', 'HP', 'HES', 'HPQ', 'HD', 'HON', 'HRL', 'HSP', 'HST', 'HCBK', 'HUM', 'HBAN', 'ITW', 'IR', 'TEG', 'INTC', 'ICE', 'IBM', 'IFF', 'IGT', 'IP', 'IPG', 'INTU', 'ISRG', 'IVZ', 'IRM', 'JBL', 'JEC', 'JDSU', 'JNJ', 'JCI', 'JOY', 'JPM', 'JNPR', 'K', 'KEY', 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KRFT', 'KR', 'LLL', 'LH', 'LRCX', 'LM', 'LEG', 'LEN', 'LUK', 'LIFE', 'LLY', 'LTD', 'LNC', 'LLTC', 'LMT', 'L', 'LO', 'LOW', 'LSI', 'LYB', 'MTB', 'M', 'MRO', 'MPC', 'MAR', 'MMC', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'MHP', 'MCK', 'MJN', 'MWV', 'MDT', 'MRK', 'MET', 'PCS', 'MCHP', 'MU', 'MSFT', 'MOLX', 'TAP', 'MDLZ', 'MON', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MUR', 'MYL', 'NBR', 'NDAQ', 'NOV', 'NTAP', 'NFLX', 'NWL', 'NFX', 'NEM', 'NWSA', 'NEE', 'NKE', 'NI', 'NE', 'NBL', 'JWN', 'NSC', 'NTRS', 'NOC', 'NU', 'NRG', 'NUE', 'NVDA', 'NYX', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'OI', 'PCAR', 'PLL', 'PH', 'PDCO', 'PAYX', 'BTU', 'JCP', 'PNR', 'PBCT', 'POM', 'PEP', 'PKI', 'PRGO', 'PETM', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PBI', 'PCL', 'PNC', 'RL', 'PPG', 'PPL', 'PX', 'PCP', 'PCLN', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'QEP', 'PWR', 'QCOM', 'DGX', 'RRC', 'RTN', 'RHT', 'RF', 'RSG', 'RAI', 'RHI', 'ROK', 'COL', 'ROP', 'ROST', 'RDC', 'R', 'SWY', 'SAI', 'CRM', 'SNDK', 'SCG', 'SLB', 'SNI', 'STX', 'SEE', 'SRE', 'SHW', 'SIAL', 'SPG', 'SLM', 'SJM', 'SNA', 'SO', 'LUV', 'SWN', 'SE', 'S', 'STJ', 'SWK', 'SPLS', 'SBUX', 'HOT', 'STT', 'SRCL', 'SYK', 'STI', 'SYMC', 'SYY', 'TROW', 'TGT', 'TEL', 'TE', 'THC', 'TDC', 'TER', 'TSO', 'TXN', 'TXT', 'HSY', 'TRV', 'TMO', 'TIF', 'TWX', 'TWC', 'TIE', 'TJX', 'TMK', 'TSS', 'TRIP', 'TSN', 'TYC', 'USB', 'UNP', 'UNH', 'UPS', 'X', 'UTX', 'UNM', 'URBN', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VZ', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WAG', 'DIS', 'WPO', 'WM', 'WAT', 'WPI', 'WLP', 'WFC', 'WDC', 'WU', 'WY', 'WHR', 'WFM', 'WMB', 'WIN', 'WEC', 'WPX', 'WYN', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XL', 'XYL', 'YHOO', 'YUM', 'ZMH', 'ZION']
    tickersMedium = ['MMM', 'ACE', 'ABT', 'ANF', 'ACN', 'ADBE', 'ADT', 'AMD', 'AES', 'AET', 'AFL', 'A', 'GAS', 'APD', 'ARG', 'AKAM', 'AA', 'ALXN', 'ATI', 'AGN', 'ALL', 'ALTR', 'MO', 'AMZN', 'AEE', 'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AMGN', 'APH', 'APC', 'ADI', 'AON', 'APA', 'AIV', 'APOL', 'AAPL', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP', 'AN', 'AZO', 'AVB', 'AVY']
    tickersSmall = ['^GSPC','MMM', 'ACE', 'ABT', 'ANF', 'ACN', 'ADBE', 'ADT', 'AMD', 'AES', 'AET']
    tickersMini = ['MMM', 'ACE']
    startdate = '2008-01-01'
    enddate = date.today()
    
    # Get rebased prices
    closePrices, seriesbegin = getAdjClosePrices(tickersSmall, startdate, enddate)
    pricesRebased = getPricesRebased(closePrices, seriesbegin, base=100, asjson=False)
    
# Matplotlib (for testing only): interactive mode
#    import matplotlib.pyplot as plt
#    import pylab
#    pylab.ion()
#    pricesRebased.plot()
    

"""
# Different Frequencies
pricesDaily = prices.asfreq('D', method='ffill')
pricesMonthly = prices.asfreq('M', method='ffill') 
pricesWeekly = prices.asfreq('W-FRI')


pricesBusinessDay = prices.asfreq('B')
# Covariance
cov = returns.cov()

corr = returns.corr()

# Standard Deviation
std = returns.std()

# Period Return
today = date(2013, 01, 18)
begOfYear = date(today.year - 1, 12, 31)

yearToDate = pricesDaily.ix[begOfYear] / prices.ix[today] - 1


# Pandas Plotting with Matplotlib
#pricesRebased['D'].plot()
#prices['D'].plot()
#prices['D']['MMM'].plot(color='red')
#prices['M']['MMM'].plot()


#pd.rolling_mean(pricesDaily['MMM'], 60, min_periods=50).plot()

# Display dataframe in PyQt Grid (for checking)
#from qtpandas import dfshow
#dfshow(prices.reset_index())

# Some quick visualizations
# Plot History
returnIndex.plot()

# Correlation Heatmap
def heatmap(df, cmap=plt.cm.jet):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    axim = ax.imshow(df.values, cmap=cmap, interpolation='nearest')
    ax.set_xlabel(df.columns.name)
    ax.set_xticks(np.arange(len(df.columns)))
    ax.set_xticklabels(list(df.columns))
    ax.set_ylabel(df.index.name)
    ax.set_yticks(np.arange(len(df.index)))
    ax.set_yticklabels(list(df.index))
    plt.colorbar(axim)
    
correlation = returns.corr()    
heatmap(correlation)

#Quickly trying out histograms
fig = plt.figure()
fig.add_subplot(2,2,1)
returns.ix[:,0].hist(bins=50)
"""
