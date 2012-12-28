"""
    Tripping Nemesis
    Program Entry Point
"""
import os, sys
from PySide import QtCore, QtGui
from log import log

sys.path.append('..')

from controller.main_controller import MainController 
"""
    Application entry point
"""
def main():
    app = QtGui.QApplication(sys.argv)
    main_form = MainController()
    main_form.Show()
    sys.exit(app.exec_())
    sys.exit()

if __name__ == '__main__':
    main()
