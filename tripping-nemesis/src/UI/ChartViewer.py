# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\src\GitHub\tripping-nemesis\tripping-nemesis\src\UI\ChartViewer.ui'
#
# Created: Tue Dec 11 09:21:14 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ChartViewer(object):
    def setupUi(self, ChartViewer):
        ChartViewer.setObjectName(_fromUtf8("ChartViewer"))
        ChartViewer.resize(671, 464)
        self.buttonBox = QtGui.QDialogButtonBox(ChartViewer)
        self.buttonBox.setGeometry(QtCore.QRect(310, 420, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(ChartViewer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChartViewer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChartViewer.reject)
        QtCore.QMetaObject.connectSlotsByName(ChartViewer)

    def retranslateUi(self, ChartViewer):
        ChartViewer.setWindowTitle(QtGui.QApplication.translate("ChartViewer", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

