"""
    Tripping Nemesis
    Program Entry Point
"""
import os, sys
from PyQt4 import QtGui, QtCore
from controller.MainController import MainController 
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
