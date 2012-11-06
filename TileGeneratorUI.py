# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from TileGeneratorUI_form import Ui_TileGenerator_UI
import TileGenerator

class TileGeneratorUI(QDialog, Ui_TileGenerator_UI):
    def __init__(self, parent, flags=None):
        QDialog.__init__(self, parent.iface.mainWindow(), flags)
        # Set up the user interface from Designer. 
        self.parent = parent
        self.setupUi(self)
        
        doubleValidator = QDoubleValidator()
        doubleValidator.setBottom(0.0001)
        self.units_pixel.setValidator(doubleValidator)
        
        intValidator = QIntValidator(1, 100)
        self.thread_count.setValidator(intValidator)
        
        QObject.connect(self.output_browse, SIGNAL("clicked()"), self.setOutputDir)
        QObject.connect(self.xml_browse, SIGNAL("clicked()"), self.setXmlFile)
        QObject.connect(self.border_browse, SIGNAL("clicked()"), self.setBorderFile)
        
    def setOutputDir(self):
        dlg = QFileDialog(self)
        dlg.setFileMode(QFileDialog.Directory)
        if dlg.exec_():
            self.output_path.setText(dlg.directory().absolutePath())

    def getSingleFile(self, nameFilter):
        dlg = QFileDialog(self)
        dlg.setNameFilter(nameFilter)
        dlg.setFileMode(QFileDialog.ExistingFile)
        if dlg.exec_():
            return str(dlg.selectedFiles()[0])
        return ""
    
    
    def setXmlFile(self):
        self.xml_file.setText(self.getSingleFile("*.xml"))
        
    def setBorderFile(self):
        self.border_file.setText(self.getSingleFile("*.shp"))
        
    def accept(self):    
        if not self.units_pixel.text().toFloat()[1]:
            return

        if not self.thread_count.text().toInt()[1]:
            return
            
        if self.output_path.text() == "":
            return
         
        if self.xml_file.text() == "":
            return
        
        if self.border_file.text() == "":
            return
                    
        TileGenerator.printMap(self.thread_count.text().toInt()[0], 
            str(self.output_path.text()), 
            self.units_pixel.text().toFloat()[0], 
            str(self.xml_file.text()), 
            str(self.border_file.text()))
        
        
        
        
        
        
        
        
        