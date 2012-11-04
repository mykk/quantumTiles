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
        QObject.connect(self.output_browse, SIGNAL("clicked()"), self.setOutputDir)
        QObject.connect(self.xml_browse, SIGNAL("clicked()"), self.setXmlFile)
        QObject.connect(self.border_browse, SIGNAL("clicked()"), self.setBorderFile)
        self.outputDir = ""
        
    def setOutputDir(self):
        dlg = QFileDialog(self)
        dlg.setFileMode(QFileDialog.Directory)
        dlg.open()
        self.outputDir = dlg.directory().absolutePath()

    def setXmlFile(self):
        i = 1
        
    def setBorderFile(self):
        x = 1