# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\src\github\assetjet\resources\ui\vw_chart.ui'
#
# Created: Wed Jan 16 13:26:30 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ChartView(object):
    def setupUi(self, ChartView):
        ChartView.setObjectName("ChartView")
        ChartView.resize(671, 464)
        self.buttonBox = QtGui.QDialogButtonBox(ChartView)
        self.buttonBox.setGeometry(QtCore.QRect(310, 420, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frmChartMain = QtGui.QFrame(ChartView)
        self.frmChartMain.setGeometry(QtCore.QRect(9, 9, 651, 401))
        self.frmChartMain.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmChartMain.setFrameShadow(QtGui.QFrame.Raised)
        self.frmChartMain.setObjectName("frmChartMain")

        self.retranslateUi(ChartView)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ChartView.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ChartView.reject)
        QtCore.QMetaObject.connectSlotsByName(ChartView)

    def retranslateUi(self, ChartView):
        ChartView.setWindowTitle(QtGui.QApplication.translate("ChartView", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

