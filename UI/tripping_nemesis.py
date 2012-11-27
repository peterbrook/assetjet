# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\tripping_nemesis.ui'
#
# Created: Tue Nov 27 15:07:47 2012
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
        self.listWidget = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout.addWidget(self.listWidget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.listWidget_2 = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.horizontalLayout.addWidget(self.listWidget_2)

        self.retranslateUi(TrippingNemesis)
        QtCore.QMetaObject.connectSlotsByName(TrippingNemesis)

    def retranslateUi(self, TrippingNemesis):
        TrippingNemesis.setWindowTitle(QtGui.QApplication.translate("TrippingNemesis", "Tripping Nemesis", None, QtGui.QApplication.UnicodeUTF8))

