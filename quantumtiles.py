# -*- coding: utf-8 -*-

import os
import tempfile
import resources
from qgis.gui import *
from qgis.core import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import mapnik

class Quantumtiles(QObject):
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        # create action that will start plugin configuration
        self.action = QAction(QIcon(":/mapPuzzle.png"), "QuantumTiles", self.iface.mainWindow())
        self.action.setWhatsThis("Generate Tiles with Qgis")
        self.action.setStatusTip("Generate Tiles")
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&QuantumTiles", self.action)

    def unload(self):
        # remove the plugin menu item and icon
        self.iface.removePluginMenu("&QuantumTiles",self.action)
        self.iface.removeToolBarIcon(self.action)


    def run(self):
        # create and show a configuration dialog or something similar
        print "TestPlugin: run called!"
