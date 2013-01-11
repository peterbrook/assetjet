"""
    {copyright}
    AssetJet
    Program Entry Point
"""
import os, sys
from PySide import QtCore, QtGui
from assetjet.log import log
from assetjet.controller.main_controller import MainController 
from assetjet.cfg import cfg
from assetjet.util import updater

def main():
        
    upd = updater.Updater(cfg.root.UpdateUrl)
    upd.daemon=True
    upd.start()
    
    app = QtGui.QApplication(sys.argv)
    mainForm = MainController()
    mainForm.Show()
    sys.exit(app.exec_())
    sys.exit(0)

if __name__ == '__main__':
    log.Debug("Initialising app")
    main()
       
    