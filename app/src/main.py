"""
    {copyright}
    AssetJet
    Program Entry Point
"""
import os, sys
import time
from PySide import QtCore, QtGui
from assetjet.log import log
from assetjet.controller.main_controller import MainController
from assetjet.util import updater
import local_server
import assetjet.view.resources_rc

def main():
    # Create MainApp
    app = QtGui.QApplication(sys.argv)
       
    # Check for Updates when run as frozen executable
    if getattr(sys,'frozen',False):
        updater.update(app)
    
    # Initialise updater Daemon    
    upd = updater.Updater(cfg.root.UpdateUrl)
    #upd.updateDialog()
# Disable threading for now
#    upd.daemon=True
#    upd.start()
    upd.run()
    
    
    # Create and display the splash screen
    # Splash screen
    splash_pix = QtGui.QPixmap(':/splashAssetJet.png') 
    splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()  
    app.processEvents()
    # Load the heavy modules here
    time.sleep(3)
    import pandas
    import numpy
    import scipy
    
    # Initialise web server to server HTML to WebView
    srv = local_server.LocalServer()
    srv.daemon=True
    srv.start()
    log.Debug("Started web server")
    
    # Launch the app and pass control to the main controller 
    mainForm = MainController()
    mainForm.show_()
    splash.finish(mainForm)
    sys.exit(app.exec_())
    sys.exit(0)

if __name__ == '__main__':
    log.Debug("Initialising app")
    main()       
    