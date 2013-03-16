# TODO: Turn into Wizard
import os, sys
from PySide import QtGui, QtCore
import assetjet.view.resources_rc
from assetjet.view.vw_db_location import Ui_db_location
from assetjet.cfg import cfg

# Dialog Window
class DbLocation(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self) 
       
        self.ui=Ui_db_location()
        self.ui.setupUi(self)

        
        # using Qt's version as os.path.expanduser('~') fails on WinPython
        self.initial_dir = os.path.abspath(os.path.join(
                                       QtCore.QDir.homePath(),'AssetJetData'))
        self.ui.location.setText(self.initial_dir)
        self.ui.button_change.clicked.connect(self.selectDir)
        
    def selectDir(self):
        QtGui.QFileDialog.whatsThis = False
        reply = QtGui.QFileDialog.getExistingDirectory(None,
                                                       'Select Directory',
                                                       self.initial_dir)
        # Leave the path unchanged if the users cancels
        if reply:        
            self.ui.location.setText(reply)
    
    def getText(self):
        return self.ui.location.text()
        
def run(app):
    dlgDbLocation=DbLocation()
    dlgDbLocation.setWindowFlags(QtCore.Qt.WindowTitleHint)
    if dlgDbLocation.exec_():
        cfg.add_entry('Database', 'DbFileName',
                      os.path.join(dlgDbLocation.getText(),'assetjet.db'))

if __name__ == "__main__":
    run()
    

 
