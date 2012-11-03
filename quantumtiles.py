# -*- coding: utf-8 -*-

import os
import resources
from qgis.gui import *
from qgis.core import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Quantumtiles(QObject):
    def __init__(self, iface):
        QObject.__init__(self)
        self.iface = iface
        self.canvas = iface.mapCanvas()

    def initGui(self):
        self.mainAction = QAction(QIcon(":/mapPuzzle.png"),"Tile Generator", self.iface.mainWindow())
        self.mainAction.setWhatsThis("Tile Generator")
        QObject.connect(self.mainAction, SIGNAL("triggered()"), self.mainActionRun)
        self.iface.addToolBarIcon(self.mainAction)
        self.iface.addPluginToMenu("Generate Tiles", self.mainAction)
        
    def unload(self):
        self.iface.removePluginMenu("Quantumtiles", self.mainAction)

    def mainActionRun(self):
        info = QString("Generate tiles with qgis.\nWritten by Mykolas Simutis\nhttps://github.com/mykk/quantumTiles")
        QMessageBox.information(self.iface.mainWindow(),"About", info)    