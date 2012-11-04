# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from TileGeneratorUI_form import Ui_TileGenerator_UI

class TileGeneratorUI(QDialog, Ui_TileGenerator_UI):
    def __init__(self, parent, flags=None):
        QDialog.__init__(self, parent.iface.mainWindow(), flags)
        # Set up the user interface from Designer. 
        self.parent = parent
        self.setupUi(self)