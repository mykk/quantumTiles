# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TileGenerator.ui'
#
# Created: Sun Nov  4 11:59:46 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TileGenerator_UI(object):
    def setupUi(self, TileGenerator_UI):
        TileGenerator_UI.setObjectName(_fromUtf8("TileGenerator_UI"))
        TileGenerator_UI.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(TileGenerator_UI)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(TileGenerator_UI)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TileGenerator_UI.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TileGenerator_UI.reject)
        QtCore.QMetaObject.connectSlotsByName(TileGenerator_UI)

    def retranslateUi(self, TileGenerator_UI):
        TileGenerator_UI.setWindowTitle(QtGui.QApplication.translate("TileGenerator_UI", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

