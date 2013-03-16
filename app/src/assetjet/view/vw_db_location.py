# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\resources\ui\vw_db_location.ui'
#
# Created: Fri Mar 15 23:25:03 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_db_location(object):
    def setupUi(self, db_location):
        db_location.setObjectName("db_location")
        db_location.resize(475, 154)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(db_location.sizePolicy().hasHeightForWidth())
        db_location.setSizePolicy(sizePolicy)
        db_location.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Pie-chart.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        db_location.setWindowIcon(icon)
        self.verticalLayoutWidget = QtGui.QWidget(db_location)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutWidget = QtGui.QWidget(db_location)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 7, 461, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.libloc_label1 = QtGui.QLabel(self.layoutWidget)
        self.libloc_label1.setWordWrap(True)
        self.libloc_label1.setObjectName("libloc_label1")
        self.verticalLayout_2.addWidget(self.libloc_label1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.location = QtGui.QLineEdit(self.layoutWidget)
        self.location.setText("")
        self.location.setFrame(True)
        self.location.setReadOnly(False)
        self.location.setPlaceholderText("")
        self.location.setObjectName("location")
        self.horizontalLayout.addWidget(self.location)
        self.button_change = QtGui.QPushButton(self.layoutWidget)
        self.button_change.setObjectName("button_change")
        self.horizontalLayout.addWidget(self.button_change)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.libloc_label2 = QtGui.QLabel(self.layoutWidget)
        self.libloc_label2.setWordWrap(True)
        self.libloc_label2.setObjectName("libloc_label2")
        self.verticalLayout_2.addWidget(self.libloc_label2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnOK = QtGui.QPushButton(self.layoutWidget)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout_3.addWidget(self.btnOK)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(db_location)
        QtCore.QObject.connect(self.btnOK, QtCore.SIGNAL("clicked()"), db_location.accept)
        QtCore.QMetaObject.connectSlotsByName(db_location)

    def retranslateUi(self, db_location):
        db_location.setWindowTitle(QtGui.QApplication.translate("db_location", "AssetJet Database Location", None, QtGui.QApplication.UnicodeUTF8))
        self.libloc_label1.setText(QtGui.QApplication.translate("db_location", "<html><head/><body><p>Choose a location for your AssetJet database:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.location.setToolTip(QtGui.QApplication.translate("db_location", "<html><head/><body><p>Press the <span style=\" font-weight:600;\">Change</span> button to edit.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.button_change.setText(QtGui.QApplication.translate("db_location", "&Change", None, QtGui.QApplication.UnicodeUTF8))
        self.libloc_label2.setText(QtGui.QApplication.translate("db_location", "If a database already exists at the new location, AssetJet will switch to using it.", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOK.setText(QtGui.QApplication.translate("db_location", "OK", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
