
import os, sys
from PyQt4 import QtGui, QtCore

sys.path.append(os.curdir + "\\UI")
from tn_mainwindow import Ui_TrippingNemesis

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = Ui_TrippingNemesis()  
        self.ui.setupUi(self)        
        self.model = QtGui.QStandardItemModel()
        
def main():
    app = QtGui.QApplication(sys.argv)
    mainForm = MainForm()
    mainForm.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()