# -*- coding: utf-8 -*-

from quantumtiles import Quantumtiles

def name():
  return "Quantumtiles"

def description():
  return "Generate Tiles using Qgis. With the help of Mapnik."

def version():
  return "Version 0.1"

def qgisMinimumVersion():
  return "1.0.0"

def authorName():
  return "Mykolas Simutis (mykolas.simutis@gmail.com)"

def homepage():
  return "https://github.com/mykk/quantumTiles"

def classFactory(iface):
  return Quantumtiles(iface)
