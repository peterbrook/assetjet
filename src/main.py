"""
    Tripping Nemesis
    Program Entry Point
    TODO: Refactor this so that it properly initialises and passes control to a Main Controller object
"""
import os, sys
from PyQt4 import QtGui, QtCore

sys.path.append('../resources/UI')
sys.path.append('../DB')

from vw_main import Ui_Main
from vw_chart import Ui_ChartView
import database

class MainForm(QtGui.QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        
        # Go borderless so it looks the same no matter what platform? TBD
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setupUi(self)
        self.model = QtGui.QStandardItemModel()
        
        #database.populate_symbol_list()
        tickers = database.all_symbols()

        for i in range(0, len(tickers)):
            
            #liTicker = self.lstSymbols.model.item(i, 0)
            liTicker = QtGui.QListWidgetItem(tickers[i])
            self.lstSymbolList.addItem(liTicker)
            
#        self.view = QtGui.QListView()
#        self.view.setModel(self.model)
#        self.view.setDragDropMode(QtGui.QAbstractItemView.InternalMove)

#        self.setCentralWidget(self.view)

def main():
    app = QtGui.QApplication(sys.argv)
    mainForm = MainForm()
    mainForm.show()
    sys.exit(app.exec_())
    sys.exit()

if __name__ == '__main__':
    main()