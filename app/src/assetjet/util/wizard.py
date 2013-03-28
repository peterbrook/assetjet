import os, sys
from PySide import QtGui, QtCore
from PySide.QtCore import Qt
from PySide.QtGui import QMessageBox
import assetjet.view.resources_rc
from assetjet.view.vw_db_location import Ui_db_location
from assetjet.cfg import cfg
from assetjet.db import download_data

# Dialog Window
class DbLocation(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self) 
       
        self.ui = Ui_db_location()
        self.ui.setupUi(self)

        # Using Qt's version as os.path.expanduser('~') fails on WinPython
        self.initial_dir = os.path.abspath(os.path.join(
                                       QtCore.QDir.homePath(),'AssetJetData'))
        self.ui.location.setText(self.initial_dir)
        self.ui.button_change.clicked.connect(self.selectDir)
        
    def selectDir(self):
        QtGui.QFileDialog.whatsThis = False
        reply = QtGui.QFileDialog.getExistingDirectory(None,
                                                       'Select Directory',
                                                       self.initial_dir)
        if reply: # Leave the path unchanged if the users cancels       
            self.ui.location.setText(reply)
            
    def getText(self):
        return self.ui.location.text()
        
def run(app):
    # Ask user for AssetJet database location
    dlgDbLocation = DbLocation()
    # Hide the 'What's This' question mark
    dlgDbLocation.setWindowFlags(QtCore.Qt.WindowTitleHint)
    if dlgDbLocation.exec_():
        loc = os.path.join(dlgDbLocation.getText(),'assetjet.db')
        # create directory if it doesn't exist yet
        if not os.path.exists(dlgDbLocation.getText()):
            os.mkdir(dlgDbLocation.getText())
        cfg.add_entry('Database', 'DbFileName', loc)
                      
    # Start download thread if database is not existing yet
    if not os.path.exists(loc):
        # Check internet connection
        from assetjet.util import util
        if util.test_url('http://finance.yahoo.com'):
            # Start download thread
            download = download_data.Downloader(loc)
            download.daemon = True
            download.start()
            
            # Create download progress dialog
            dlgProgress = QtGui.QProgressDialog(
                                labelText='Downloading 1 year of daily returns for members of the S&P 500. \n This may take a couple of minutes.\n' ,
                                minimum = 0, maximum = 500,
                                flags=Qt.CustomizeWindowHint | Qt.WindowTitleHint)
            dlgProgress.setWindowTitle('Downloading...')                                       
            dlgProgress.setCancelButton(None)
            dlgProgress.setWindowIcon(QtGui.QIcon(':/Pie-chart.ico'))
            dlgProgress.show()
    
            # Update progress bar through signal
            download.downloaded.connect(dlgProgress.setValue)
            download.finished.connect(dlgProgress.close)
            app.exec_()  
            
            # TODO: let it run in parallel with the local server thread
            download.wait()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('No Internet Connection')
            msgBox.setText("To run AssetJet the first time, you need a working \n" \
                           "internet connection to download the historical returns.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.setWindowIcon(QtGui.QIcon(':/Pie-chart.ico'))
            reply = msgBox.exec_()
            sys.exit()

 
