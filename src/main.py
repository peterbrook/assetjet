"""
    Tripping Nemesis
    Program Entry Point
    TODO: Refactor this so that it properly initialises and passes control to a Main Controller object
"""
import os, sys

from PyQt4 import QtGui, QtCore

import cfg
from controller import *
from controller.MainController import MainController 

defaultDbFileName = None

"""
    Application entry point
"""
def main():
    
    app = QtGui.QApplication(sys.argv)
    mainForm = MainController()
    mainForm.Show()
    sys.exit(app.exec_())
    sys.exit()

if __name__ == '__main__':
    main()