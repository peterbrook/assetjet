# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\src\GitHub\tripping-nemesis\tripping-nemesis\src\UI\tn_mainwindow.browser.ui'
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

class Ui_TrippingNemesis(object):
    def setupUi(self, TrippingNemesis):
        TrippingNemesis.setObjectName(_fromUtf8("TrippingNemesis"))
        TrippingNemesis.setWindowModality(QtCore.Qt.ApplicationModal)
        TrippingNemesis.resize(599, 485)
        self.horizontalLayoutWidget = QtGui.QWidget(TrippingNemesis)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 19, 561, 441))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.webMain = QtWebKit.QWebView(self.horizontalLayoutWidget)
        self.webMain.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webMain.setObjectName(_fromUtf8("webMain"))
        self.horizontalLayout.addWidget(self.webMain)
        self.listWidget_2 = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.horizontalLayout.addWidget(self.listWidget_2)

        self.retranslateUi(TrippingNemesis)
        QtCore.QMetaObject.connectSlotsByName(TrippingNemesis)

    def retranslateUi(self, TrippingNemesis):
        TrippingNemesis.setWindowTitle(QtGui.QApplication.translate("TrippingNemesis", "Tripping Nemesis", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
