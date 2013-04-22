import os
from PySide import QtGui, QtCore
from assetjet.view.vw_main import Ui_Main
from assetjet.util import util
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
        
