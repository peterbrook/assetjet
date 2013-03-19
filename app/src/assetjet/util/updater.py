import sys, os
import esky
from assetjet.log import log  
from PySide import QtGui
from PySide.QtGui import QMessageBox
from PySide.QtCore import QThread, Qt
from assetjet.cfg import cfg

class Updater(QThread):
    """
    This class encapsulates multi-threaded logic for updating the
    application using Esky
    """
    
    def __init__(self, url):
        QThread.__init__(self)
        self.url = url
        self.new_version = None 
        self.frozenapp = esky.Esky(sys.executable, self.url)
        try:
            log.Debug('Checking for new version at {0}'.format(self.url))
            self.new_version = self.frozenapp.find_update()
        except Exception, e:
            log.Error(str(e))
    
    def updateDialog(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Update available')
        msgBox.setText("There is a new version of AssetJet available.\n" \
                       "Do you want to download and install?")
        msgBox.setStandardButtons(QMessageBox.Yes | QtGui.QMessageBox.No)
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setDefaultButton(QMessageBox.Yes)
        msgBox.setWindowIcon(QtGui.QIcon(':/Pie-chart.ico'))
        reply = msgBox.exec_()
        return reply

    def run(self):
        self.frozenapp.auto_update()
        appexe = esky.util.appexe_from_executable(sys.executable)
        os.execv(appexe,[appexe] + sys.argv[1:])

def update(app):     
    upd = Updater(cfg.root.UpdateUrl)
    upd.daemon = True
    upd.frozenapp.cleanup() # delete the folder of the previous version
    if upd.new_version:
        reply = upd.updateDialog()
    
        if reply == QtGui.QMessageBox.Yes:
            upd.start()
            dlgProgress = QtGui.QProgressDialog(
                                labelText='Updating AssetJet, stay tuned...',
                                minimum = 0, maximum = 0,
                                flags=Qt.WindowTitleHint)
            dlgProgress.setWindowTitle('AssetJet Update')                                            
            dlgProgress.setCancelButton(None)
            dlgProgress.setWindowIcon(QtGui.QIcon(':/Pie-chart.ico'))
            dlgProgress.show()
            
            upd.finished.connect(dlgProgress.close)
            app.exec_()  
               
