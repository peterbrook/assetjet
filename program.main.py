
import os, sys
from PyQt4 import QtGui, QtCore

sys.path.append(os.curdir + "\\UI")
from tripping_nemesis import Ui_TrippingNemesis

class MainForm(QtGui.QMainWindow, Ui_TrippingNemesis):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        
        self.model = QtGui.QStandardItemModel()
        self.height = 800
        
        for k in range(0, 4):
            parentItem = self.model.invisibleRootItem()
            for i in range(0, 4):
                item = QtGui.QStandardItem(QtCore.QString("item %0 %1").arg(k).arg(i))
                parentItem.appendRow(item)
                parentItem = item

        self.view = QtGui.QListView()
        self.view.setModel(self.model)
        self.view.setDragDropMode(QtGui.QAbstractItemView.InternalMove)

        self.setCentralWidget(self.view)

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.height = 1000
    form.width = 1200
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()