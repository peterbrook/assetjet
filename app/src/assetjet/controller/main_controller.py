import os
from PySide import QtGui, QtCore
import sqlalchemy.orm as orm
from assetjet.view.vw_main import Ui_Main
from assetjet.log import log
from assetjet.util import util
#from assetjet.model import asset
from assetjet import __version__

class MainController(QtGui.QMainWindow):

    eventsInitialised = False
            
    def __init__(self, parent=None):
        super(MainController, self).__init__(parent)
            
    def show_(self):        
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        mainPath = os.path.join(util.getBaseDir(), 'httpdocs', 'main.html')
        mainUrl = QtCore.QUrl.fromLocalFile(mainPath)
        self.ui.webView.load(mainUrl)
        self.ui.webView.url = mainUrl
        self.show()
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle('AssetJet {0}'.format(__version__))

        """
        tickers = self.GetAllSymbols()

        for i in range(0, len(tickers)):            
            #liTicker = self.lstSymbols.model.item(i, 0)
            liTicker = QtGui.QListWidgetItem(tickers[i].name)
            self.ui.lstSymbolList.addItem(liTicker)
        """

               