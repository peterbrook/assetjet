
import os, sys
from PyQt4 import QtGui, QtCore

sys.path.append(os.curdir + "\\UI")
from tripping_nemesis import Ui_TrippingNemesis

class MainForm(QtGui.QMainWindow, Ui_TrippingNemesis):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.model = QtGui.QStandardItemModel()
        
def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.height = 1000
    form.width = 1200
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()