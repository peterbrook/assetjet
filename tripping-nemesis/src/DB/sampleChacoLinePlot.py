import time
tic = time.time()

# ETS imports (non-chaco)
from enable.component_editor import ComponentEditor
from traits.api import HasTraits, Instance, Int, List, Str, Enum, Any, DelegatesTo
from traitsui.api import Item, View
from enable.api import Component, ComponentEditor, BaseTool
from chaco.tools.cursor_tool import CursorTool, BaseCursorTool

# Chaco imports
from chaco.api import ArrayPlotData, Plot, PlotAxis, create_line_plot
from chaco.scales.api import CalendarScaleSystem
from chaco.scales_tick_generator import ScalesTickGenerator
from chaco.tools.api import PanTool, ZoomTool, RangeSelection, \
        RangeSelectionOverlay, LegendTool
import pandas.io.sql as sql
import sqlite3
import numpy as np

print('imports: %s') % str(time.time() - tic)
tic = time.time()

# SQLite Database
db = 'TimeSeries.db'

# Create a DataFrame from a SQL query 
conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
prices = sql.read_frame("""SELECT Cd, Date, Close, AdjClose
                           FROM TimeSeries WHERE Cd = 'MMM'
                           """, conn)
c = conn.cursor()
c.execute("""SELECT (JULIANDAY(Date) - 2440587.5)*86400.0  AS Dte
                           FROM TimeSeries
                           WHERE Cd = 'MMM'""")

dateArray = np.asarray(c.fetchall(), dtype = float)
conn.close()

print('sqlite: %s') % str(time.time() - tic)
tic = time.time()

# Pivot DataFrame to work easily with the time series
pricesPivot = prices.pivot('Date', 'Cd', 'Close')
returns = pricesPivot.pct_change()
returnIndex = (1 + returns).cumprod()
returnIndex.values[:1] = 1
returnIndex = returnIndex * 100
data = pricesPivot.values

print('pandas: %s') % str(time.time() - tic)
tic = time.time()

class PlotApp(HasTraits):

    plotdata = Instance(ArrayPlotData)
    symbols = List()

    returns_plot = Instance(Plot)
    times_ds = Any()   # arraydatasource for the time axis data

    traits_view = View(
            Item('returns_plot', editor=ComponentEditor(), show_label = False),
            width=1024, height=500,
            resizable=True,
            title = "Historical Returns")

    def __init__(self, symbols, **kwtraits):
        super(PlotApp, self).__init__(symbols=symbols, **kwtraits)
        self._create_data(symbols)
        self._create_returns_plot()
        if len(self.symbols) > 1:
            self.sym2 = self.symbols[1]
        return

    def _create_returns_plot(self):
        plot = Plot(self.plotdata)
        plot.legend.visible = False
        plot.x_axis = None
        x_axis = PlotAxis(plot, orientation="bottom",
                        tick_generator=ScalesTickGenerator(scale=CalendarScaleSystem()))
        plot.overlays.append(x_axis)
        plot.x_grid.tick_generator = x_axis.tick_generator
        for i, name in enumerate(self.plotdata.list_data()):
            if name == "times":
                continue
            renderer = plot.plot(("times", name), type="line", name=name,
                                  color="auto", line_width=2)[0]
        self.times_ds = renderer.index
        print('chaco: %s') % str(time.time() - tic)
        
      
        
        
        # Tricky: need to set auto_handle_event on the RangeSelection
        # so that it passes left-clicks to the PanTool
        # FIXME: The range selection is still getting the initial left down
        renderer.tools.append(RangeSelection(renderer, left_button_selects = False,
            auto_handle_event = False))
        plot.tools.append(PanTool(plot, drag_button="left", constrain=True,
            constrain_direction="x"))
        plot.overlays.append(ZoomTool(plot, tool_mode="range", max_zoom_out=1.0))
        # Attach the range selection to the last renderer; any one will do
        self._range_selection_overlay = RangeSelectionOverlay(renderer,
                                    metadata_name="selections")
        renderer.overlays.append(self._range_selection_overlay)
        # Grab a reference to the Time axis datasource and add a listener to its
        # selections metadata
        self.times_ds = renderer.index
        self.times_ds.on_trait_change(self._selections_changed, 'metadata_changed')
        
      
        
        
        
        
        self.returns_plot = plot

    def _create_data(self, names):
        plotdata = ArrayPlotData(times = np.squeeze(dateArray))
        i = 0
        for name in names:
            plotdata.set_data(name, data[:,i])
            i += 1
        self.plotdata = plotdata

    def _selections_changed(self, event):
        selections = event["selections"]
        low, high = selections
#        data = self.times_ds.get_data()
        self.corr_plot.request_redraw()    
    
    
    
#demo = PlotApp(['MMM', 'ACE', 'ABT', 'ANF', 'ACN', 'ADBE', 'ADT', 'AMD', 'AES', 'AET', 'AFL', 'A', 'GAS', 'APD', 'ARG', 'AKAM', 'AA', 'ALXN', 'ATI', 'AGN', 'ALL', 'ALTR', 'MO', 'AMZN', 'AEE', 'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AMGN', 'APH', 'APC', 'ADI', 'AON', 'APA', 'AIV', 'APOL', 'AAPL', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP', 'AN', 'AZO', 'AVB', 'AVY', 'AVP', 'BHI', 'BLL', 'BAC', 'BK', 'BCR', 'BAX', 'BBT', 'BEAM', 'BDX', 'BBBY', 'BMS', 'BRK.B', 'BBY', 'BIG', 'BIIB', 'BLK', 'HRB', 'BMC', 'BA', 'BWA', 'BXP', 'BSX', 'BMY', 'BRCM', 'BF.B', 'CHRW', 'CA', 'CVC', 'COG', 'CAM', 'CPB', 'COF', 'CAH', 'CFN', 'KMX', 'CCL', 'CAT', 'CBG', 'CBS', 'CELG', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHK', 'CVX', 'CMG', 'CB', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CTXS', 'CLF', 'CLX', 'CME', 'CMS', 'COH', 'KO', 'CCE', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CSC', 'CAG', 'COP', 'CNX', 'ED', 'STZ', 'CBE', 'GLW', 'COST', 'CVH', 'COV', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DF', 'DE', 'DELL', 'DNR', 'XRAY', 'DVN', 'DO', 'DTV', 'DFS', 'DISCA', 'DLTR', 'D', 'RRD', 'DOV', 'DOW', 'DPS', 'DTE', 'DD', 'DUK', 'DNB', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMC', 'EMR', 'ESV', 'ETR', 'EOG', 'EQT', 'EFX', 'EQR', 'EL', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'XOM', 'FFIV', 'FDO', 'FAST', 'FII', 'FDX', 'FIS', 'FITB', 'FHN', 'FSLR', 'FE', 'FISV', 'FLIR', 'FLS', 'FLR', 'FMC', 'FTI', 'F', 'FRX', 'FOSL', 'BEN', 'FCX', 'FTR', 'GME', 'GCI', 'GPS', 'GD', 'GE', 'GIS', 'GPC', 'GNW', 'GILD', 'GS', 'GT', 'GOOG', 'GWW', 'HAL', 'HOG', 'HAR', 'HRS', 'HIG', 'HAS', 'HCP', 'HCN', 'HNZ', 'HP', 'HES', 'HPQ', 'HD', 'HON', 'HRL', 'HSP', 'HST', 'HCBK', 'HUM', 'HBAN', 'ITW', 'IR', 'TEG', 'INTC', 'ICE', 'IBM', 'IFF', 'IGT', 'IP', 'IPG', 'INTU', 'ISRG', 'IVZ', 'IRM', 'JBL', 'JEC', 'JDSU', 'JNJ', 'JCI', 'JOY', 'JPM', 'JNPR', 'K', 'KEY', 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KRFT', 'KR', 'LLL', 'LH', 'LRCX', 'LM', 'LEG', 'LEN', 'LUK', 'LIFE', 'LLY', 'LTD', 'LNC', 'LLTC', 'LMT', 'L', 'LO', 'LOW', 'LSI', 'LYB', 'MTB', 'M', 'MRO', 'MPC', 'MAR', 'MMC', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'MHP', 'MCK', 'MJN', 'MWV', 'MDT', 'MRK', 'MET', 'PCS', 'MCHP', 'MU', 'MSFT', 'MOLX', 'TAP', 'MDLZ', 'MON', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MUR', 'MYL', 'NBR', 'NDAQ', 'NOV', 'NTAP', 'NFLX', 'NWL', 'NFX', 'NEM', 'NWSA', 'NEE', 'NKE', 'NI', 'NE', 'NBL', 'JWN', 'NSC', 'NTRS', 'NOC', 'NU', 'NRG', 'NUE', 'NVDA', 'NYX', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'OI', 'PCAR', 'PLL', 'PH', 'PDCO', 'PAYX', 'BTU', 'JCP', 'PNR', 'PBCT', 'POM', 'PEP', 'PKI', 'PRGO', 'PETM', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PBI', 'PCL', 'PNC', 'RL', 'PPG', 'PPL', 'PX', 'PCP', 'PCLN', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'QEP', 'PWR', 'QCOM', 'DGX', 'RRC', 'RTN', 'RHT', 'RF', 'RSG', 'RAI', 'RHI', 'ROK', 'COL', 'ROP', 'ROST', 'RDC', 'R', 'SWY', 'SAI', 'CRM', 'SNDK', 'SCG', 'SLB', 'SNI', 'STX', 'SEE', 'SRE', 'SHW', 'SIAL', 'SPG', 'SLM', 'SJM', 'SNA', 'SO', 'LUV', 'SWN', 'SE', 'S', 'STJ', 'SWK', 'SPLS', 'SBUX', 'HOT', 'STT', 'SRCL', 'SYK', 'STI', 'SYMC', 'SYY', 'TROW', 'TGT', 'TEL', 'TE', 'THC', 'TDC', 'TER', 'TSO', 'TXN', 'TXT', 'HSY', 'TRV', 'TMO', 'TIF', 'TWX', 'TWC', 'TIE', 'TJX', 'TMK', 'TSS', 'TRIP', 'TSN', 'TYC', 'USB', 'UNP', 'UNH', 'UPS', 'X', 'UTX', 'UNM', 'URBN', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VZ', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WAG', 'DIS', 'WPO', 'WM', 'WAT', 'WPI', 'WLP', 'WFC', 'WDC', 'WU', 'WY', 'WHR', 'WFM', 'WMB', 'WIN', 'WEC', 'WPX', 'WYN', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XL', 'XYL', 'YHOO', 'YUM'])
demo = PlotApp(['MMM'])

if __name__ == "__main__":
    demo.configure_traits()
