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
        self.output_path.setText(dlg.directory().absolutePath())

    def getSingleFile(self, nameFilter):
        dlg = QFileDialog(self)
        dlg.setNameFilter(nameFilter)
        dlg.setFileMode(QFileDialog.ExistingFile)
        dlg.open()

        if dlg.selectedFiles().isEmpty():
            return ''
        else:
            return dlg.selectedFiles()[0]
            
    def setXmlFile(self):
        self.xml_file.setText(self.getSingleFile("*.xml"))
        
    def setBorderFile(self):
        self.border_file.setText(self.getSingleFile("*.shp"))