import os
from PySide import QtGui, QtCore
from assetjet.view.vw_main import Ui_Main
from assetjet.cfg import db
from assetjet.log import log
from assetjet.util import util
from assetjet import local_server
import sqlalchemy.orm as orm

from assetjet.model import asset

class MainController(QtGui.QMainWindow):

    eventsInitialised = False
            
    def __init__(self, parent=None):
        super(MainController, self).__init__(parent)
            
    def Show(self):
        # Go borderless so it looks the same no matter what platform? TBD
        
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        mainPath = os.path.join(util.getBaseDir(), 'web', 'main.html')
        print mainPath
                            
        mainUrl = QtCore.QUrl.fromLocalFile(mainPath)
        print mainUrl
        #self.ui.webView.load(QtCore.QUrl('file://C:\src\github\assetjet\app\src\assetjet\view\vw_main.htm'))
        self.ui.webView.load(mainUrl)
        print(self.ui.webView.url())
        self.ui.webView.url = mainUrl
        print(self.ui.webView.url)
        super(QtGui.QMainWindow, self).show()
        super(QtGui.QMainWindow, self).setWindowState(QtCore.Qt.WindowMaximized)

        """
        tickers = self.GetAllSymbols()

        for i in range(0, len(tickers)):            
            #liTicker = self.lstSymbols.model.item(i, 0)
            liTicker = QtGui.QListWidgetItem(tickers[i].name)
            self.ui.lstSymbolList.addItem(liTicker)
        """
        
    def GetAllSymbols(self):
        Session = orm.sessionmaker(bind=db.GetEngine())        
        session = Session()
        return session.query(asset.Asset).all()


    def InitialiseEvents(self):
        self.connect(self.ui.lstSymbolList, SIGNAL("doubleClicked()", self.AddSymbol))
        
    def AddSymbol(self):
        QtGui.QMessageBox.critical("Hello")
        pass
               