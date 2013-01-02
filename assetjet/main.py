"""
    AssetJet
    Program Entry Point
"""
import os, sys
from PySide import QtCore, QtGui
from controller.main_controller import MainController 
import esky

sys.path.append('..')

###
# TODO: Very quick POC for Esky - needs to be refactored into silent update in
# a background thread...
if getattr(sys,"frozen",False):
    try:        
        frozenapp = esky.Esky(sys.executable,"http://localhost:8000")
        new_version = frozenapp.find_update()
        if(new_version != None):
            frozenapp.auto_update()
            appexe = esky.util.appexe_from_executable(sys.executable)
            os.execv(appexe,[appexe] + sys.argv[1:])
    except Exception, e:
        print "ERROR UPDATING APP:", e
    frozenapp.cleanup()   
###

def main():
    app = QtGui.QApplication(sys.argv)
    main_form = MainController()
    main_form.Show()
    sys.exit(app.exec_())
    sys.exit()

if __name__ == '__main__':
    main()
