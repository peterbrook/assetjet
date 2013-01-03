# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\DEV\GitHub\tripping-nemesis\resources\ui\vw_main.ui'
#
# Created: Sun Dec 23 22:48:30 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(734, 581)
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 711, 471))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lstSymbolList = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.lstSymbolList.setDragEnabled(True)
        self.lstSymbolList.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.lstSymbolList.setAlternatingRowColors(True)
        self.lstSymbolList.setObjectName("lstSymbolList")
        self.horizontalLayout.addWidget(self.lstSymbolList)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.trvwSelectedSymbols = QtGui.QTreeWidget(self.horizontalLayoutWidget)
        self.trvwSelectedSymbols.setDragEnabled(True)
        self.trvwSelectedSymbols.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.trvwSelectedSymbols.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.trvwSelectedSymbols.setAlternatingRowColors(True)
        self.trvwSelectedSymbols.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.trvwSelectedSymbols.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.trvwSelectedSymbols.setObjectName("trvwSelectedSymbols")
        self.trvwSelectedSymbols.headerItem().setText(0, "1")
        self.horizontalLayout.addWidget(self.trvwSelectedSymbols)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 711, 51))
        self.groupBox.setObjectName("groupBox")
        self.dtStartDate = QtGui.QDateEdit(self.groupBox)
        self.dtStartDate.setGeometry(QtCore.QRect(160, 20, 110, 22))
        self.dtStartDate.setObjectName("dtStartDate")
        self.btnAnalyse = QtGui.QPushButton(self.groupBox)
        self.btnAnalyse.setGeometry(QtCore.QRect(620, 20, 75, 23))
        self.btnAnalyse.setObjectName("btnAnalyse")
        self.dtEndDate = QtGui.QDateEdit(self.groupBox)
        self.dtEndDate.setGeometry(QtCore.QRect(400, 20, 110, 22))
        self.dtEndDate.setObjectName("dtEndDate")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(QtGui.QApplication.translate("Main", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Main", "Analysis Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAnalyse.setText(QtGui.QApplication.translate("Main", "Analyze", None, QtGui.QApplication.UnicodeUTF8))

