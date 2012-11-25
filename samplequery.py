#import price_db
import database
import pandas.io.sql as sql
import sqlite3

# SQLite Database
db = 'Stocks.db'
updateDatabase = False

# Populate database with some data from Yahoo! Finance
if updateDatabase:
    tickers = ['GOOG', 'MSFT', 'AAPL', 'UBSN.VX']
    database.populate_db(tickers, '2008-1-1', '2012-11-25', dbfilename=db)

# Create a DataFrame from a SQL query 
conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
df = sql.read_frame("""SELECT symbol, date, adjclose FROM stocks""", conn)
conn.close()

# Pivot DataFrame to work easily with the time series
dfPivot = df.pivot('date', 'symbol', 'adjclose')
returns = dfPivot.pct_change()
returnIndex = (1 + returns).cumprod()
returnIndex.values[:1] = 1
returnIndex.plot()

