"""
    {copyright}
    AssetJet
    Program Entry Point
"""
import os, sys
from PySide import QtCore, QtGui
from assetjet.log import log

def main():
    from assetjet.controller.main_controller import MainController 
    from assetjet.cfg import cfg
    from assetjet.util import updater
        
    upd = updater.Updater(cfg.root.UpdateUrl)
    upd.setDaemon(daemonic=True)
    upd.start()
    
    app = QtGui.QApplication(sys.argv)
    mainForm = MainController()
    mainForm.Show()
    sys.exit(app.exec_())
    sys.exit()

if __name__ == '__main__':
    if getattr(sys,"frozen",False):
    # if app is a frozen executable, use logging
        try:
            log.Debug("Initialising app")
            main()
            sys.exit(0)
           
        except Exception, ex:
            log.Error("Error in application: {0}", str(ex))
            sys.exit(-1)
    else:
    # don't use logging for debugging
        main()


    
    
    