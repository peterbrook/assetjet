# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\src\github\assetjet\resources\ui\vw_main.ui'
#
# Created: Wed Jan 16 13:26:31 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(775, 589)
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setMinimumSize(QtCore.QSize(709, 519))
        self.webView.setUrl(QtCore.QUrl("http://www.google.ch/"))
        self.webView.setObjectName("webView")
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(QtGui.QApplication.translate("Main", "AssetJet", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
