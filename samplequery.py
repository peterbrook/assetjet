#import price_db
import database
import pandas.io.sql as sql
import sqlite3

# SQLite Database
db = 'Stocks.db'

# Populate database with some data from Yahoo! Finance
tickers = ['GOOG', 'MSFT', 'AAPL', 'UBSN.VX']
database.populate_db(tickers, '2008-1-1', '2012-11-25', dbfilename=db)

# Create a DataFrame from a SQL query 
conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
df = sql.read_frame("""SELECT symbol, date, adjclose FROM stocks""", conn, index_col=['symbol', 'date'])
conn.close()

# Unstack DataFrame into to have a easy to work time series
dfUnstacked = df.unstack('symbol')
print dfUnstacked.tail()
