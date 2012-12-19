from PyQt4 import QtGui
from view.vw_main import Ui_Main
from cfg import DB
import sqlalchemy.orm as orm

from model import symbol

class MainController(QtGui.QMainWindow):
            
    def __init__(self, parent=None):
        super(QtGui.QMainWindow, self).__init__(parent)
            
    def Show(self):
        # Go borderless so it looks the same no matter what platform? TBD
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        tickers = self.GetAllSymbols()

        for i in range(0, len(tickers)):
            
            #liTicker = self.lstSymbols.model.item(i, 0)
            liTicker = QtGui.QListWidgetItem(tickers[i])
            self.ui.lstSymbolList.addItem(liTicker)

    def GetAllSymbols(self):
        Session = orm.sessionmaker(bind=DB.GetEngine())        
        session = Session()
        return session.query(symbol.Symbol).all()
               