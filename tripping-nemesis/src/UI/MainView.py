# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\src\GitHub\tripping-nemesis\tripping-nemesis\src\UI\MainView.ui'
#
# Created: Tue Dec 11 09:21:15 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName(_fromUtf8("Main"))
        Main.resize(734, 581)
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 711, 471))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lstSymbolList = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.lstSymbolList.setDragEnabled(True)
        self.lstSymbolList.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.lstSymbolList.setAlternatingRowColors(True)
        self.lstSymbolList.setObjectName(_fromUtf8("lstSymbolList"))
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
        self.trvwSelectedSymbols.setObjectName(_fromUtf8("trvwSelectedSymbols"))
        self.trvwSelectedSymbols.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout.addWidget(self.trvwSelectedSymbols)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 711, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.dtStartDate = QtGui.QDateEdit(self.groupBox)
        self.dtStartDate.setGeometry(QtCore.QRect(160, 20, 110, 22))
        self.dtStartDate.setObjectName(_fromUtf8("dtStartDate"))
        self.btnAnalyse = QtGui.QPushButton(self.groupBox)
        self.btnAnalyse.setGeometry(QtCore.QRect(620, 20, 75, 23))
        self.btnAnalyse.setObjectName(_fromUtf8("btnAnalyse"))
        self.dtEndDate = QtGui.QDateEdit(self.groupBox)
        self.dtEndDate.setGeometry(QtCore.QRect(400, 20, 110, 22))
        self.dtEndDate.setObjectName(_fromUtf8("dtEndDate"))
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Main.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Main)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(QtGui.QApplication.translate("Main", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Main", "Analysis Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAnalyse.setText(QtGui.QApplication.translate("Main", "Analyze", None, QtGui.QApplication.UnicodeUTF8))

