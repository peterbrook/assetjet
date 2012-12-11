<<<<<<< HEAD
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\src\GitHub\tripping-nemesis\tripping-nemesis\src\UI\vw_chart.ui'
#
# Created: Tue Dec 11 09:21:17 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ChartView(object):
    def setupUi(self, ChartView):
        ChartView.setObjectName(_fromUtf8("ChartView"))
        ChartView.resize(671, 464)
        self.buttonBox = QtGui.QDialogButtonBox(ChartView)
        self.buttonBox.setGeometry(QtCore.QRect(310, 420, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.frmChartMain = QtGui.QFrame(ChartView)
        self.frmChartMain.setGeometry(QtCore.QRect(9, 9, 651, 401))
        self.frmChartMain.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmChartMain.setFrameShadow(QtGui.QFrame.Raised)
        self.frmChartMain.setObjectName(_fromUtf8("frmChartMain"))

        self.retranslateUi(ChartView)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChartView.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChartView.reject)
        QtCore.QMetaObject.connectSlotsByName(ChartView)

    def retranslateUi(self, ChartView):
        ChartView.setWindowTitle(QtGui.QApplication.translate("ChartView", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

=======
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\src\GitHub\tripping-nemesis\tripping-nemesis\src\UI\vw_chart.ui'
#
# Created: Tue Dec 11 09:21:17 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ChartView(object):
    def setupUi(self, ChartView):
        ChartView.setObjectName(_fromUtf8("ChartView"))
        ChartView.resize(671, 464)
        self.buttonBox = QtGui.QDialogButtonBox(ChartView)
        self.buttonBox.setGeometry(QtCore.QRect(310, 420, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.frmChartMain = QtGui.QFrame(ChartView)
        self.frmChartMain.setGeometry(QtCore.QRect(9, 9, 651, 401))
        self.frmChartMain.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmChartMain.setFrameShadow(QtGui.QFrame.Raised)
        self.frmChartMain.setObjectName(_fromUtf8("frmChartMain"))

        self.retranslateUi(ChartView)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChartView.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChartView.reject)
        QtCore.QMetaObject.connectSlotsByName(ChartView)

    def retranslateUi(self, ChartView):
        ChartView.setWindowTitle(QtGui.QApplication.translate("ChartView", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

>>>>>>> f603b51d879d749ada65ed0bbb576e7658990349
