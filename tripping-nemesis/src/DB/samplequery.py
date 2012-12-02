import pandas.io.sql as sql
import sqlite3
import numpy as np

# Import Matplotlib in interactive mode
import matplotlib.pyplot as plt
from pylab import *
ion()

# SQLite Database
db = 'TimeSeries.db'

# Create a DataFrame from a SQL query 
conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
prices = sql.read_frame("""SELECT Cd, Date, Open, AdjClose
                           FROM TimeSeries
                           WHERE Cd IN('MMM', 'ACE', 'ABT')""", conn)
conn.close()

# Pivot DataFrame to work easily with the time series
px = ['AdjClose']
for i in px:
    pricesPivot = prices.pivot('Date', 'Cd', i)
    returns = pricesPivot.pct_change()
    returnIndex = (1 + returns).cumprod()
    returnIndex.values[:1] = 1
    returnIndex = returnIndex * 100
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
fig.add_subplot(2,2,2)
returns.ix[:,0].hist(bins=50)
fig.add_subplot(2,2,3)
returns.ix[:,0].hist(bins=50)
fig.add_subplot(2,2,4)
returns.ix[:,0].hist(bins=50)