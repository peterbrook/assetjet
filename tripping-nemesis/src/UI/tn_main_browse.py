# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\src\GitHub\tripping-nemesis\tripping-nemesis\src\UI\tn_main_browse.ui'
#
# Created: Tue Dec 11 09:21:16 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_tn_web(object):
    def setupUi(self, tn_web):
        tn_web.setObjectName(_fromUtf8("tn_web"))
        tn_web.setWindowModality(QtCore.Qt.ApplicationModal)
        tn_web.resize(599, 485)
        self.horizontalLayoutWidget = QtGui.QWidget(tn_web)
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

        self.retranslateUi(tn_web)
        QtCore.QMetaObject.connectSlotsByName(tn_web)

    def retranslateUi(self, tn_web):
        tn_web.setWindowTitle(QtGui.QApplication.translate("tn_web", "Tripping Nemesis", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
