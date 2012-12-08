from traits.api import HasTraits, Instance
from traitsui.api import View, Item
from chaco.api import Plot, ArrayPlotData
from enable.component_editor import ComponentEditor
from numpy import linspace, sin, asarray, arange
import sqlite3
from chaco.tools.api import PanTool, ZoomTool

class LinePlot(HasTraits):
    plot = Instance(Plot)

    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")

    def __init__(self):
        super(LinePlot, self).__init__()
        
        ### Get Data
        db = 'TimeSeries.db'
        conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
        cursor = conn.cursor()
        
        cursor.execute("SELECT Close, AdjClose FROM TimeSeries WHERE Cd IN('MMM')") 
        data = asarray(cursor.fetchall(), dtype = float)
        
        cursor.close()
        conn.close()
                
        x = arange(len(data))
        
        for i in range(2):
            y = data[:,i]
            plotdata = ArrayPlotData(x=x, y=y)
            plot = Plot(plotdata)
            plot.plot(("x", "y"), type="line", color="blue")
            
        
        plot.title = "TimeSeries"

        self.plot = plot
        
        plot.tools.append(PanTool(plot))
        zoom = ZoomTool(component=plot, tool_mode="box", always_on=False)
        plot.overlays.append(zoom)
        
        
        # Matplotlib
#        import matplotlib.pyplot as plt
#        import pylab
#        pylab.ion()
#        pylab.plot(x,y)        
        

if __name__ == "__main__":
    LinePlot().configure_traits()
    
    
    
