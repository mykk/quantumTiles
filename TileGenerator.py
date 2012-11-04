import sys
import os 
import argparse
import thread

from osgeo import ogr
from osgeo import gdal
import mapnik

from gdalconst import *
    
def resizePNG(sourceName, cutOffPixels, w, h):
    os.system('gdal_translate -of png -outsize 20% 20% -srcwin ' + str(cutOffPixels) + ' ' + str(cutOffPixels) + ' ' + str(w) + ' ' +  str(h) + ' '+
        sourceName +'.png ' + sourceName +'_resized.png')
    return sourceName +'_resized.png'
    

def png2tiff(sourceName, metersPerPixel, additional, w, h):
    cutOffPixels = additional / metersPerPixel
    wNew = w - cutOffPixels*2
    hNew = h - cutOffPixels*2
    resizedPng = resizePNG(sourceName, cutOffPixels, wNew, hNew)
    print "Image resized " + resizedPng +"\n"
    format = 'GTiff'
    png_driver = gdal.GetDriverByName('PNG')
    dataset = gdal.Open(resizedPng, GA_ReadOnly)
    gtiffDriver = gdal.GetDriverByName("GTiff")
    newFile = gtiffDriver.CreateCopy(sourceName + '.tif', dataset, 0, ["TILED=YES", "-b 1", "BLOCKXSIZE=512", "BLOCKYSIZE=512", "COMPRESS=LZW"])
    newFile = None
    dataset = None
    png_driver.Delete(sourceName + '.png')
    png_driver.Delete(resizedPng)



def worldMap(destination, i, j, scale, xMinimum, yMaximum):
    fileName = destination + str(scale) +'m_' + str(i) + '_' + str(j) + ".pngw"
    f = open(fileName, 'w')
    f.write(str(scale) + '\n')
    f.write(str(0) + '\n')
    f.write(str(0) + '\n')
    f.write('-' + str(scale) + '\n')
    f.write(str(xMinimum + scale/2) + '\n')
    f.write(str(yMaximum - scale/2))
    f.close()
    return fileName
    
    
def mapPrintThread(threadNo, scale, destination, xmlfile, borderFilePath):
    additional = 2560*scale

    w,h = 5120*2 + additional*2/scale, 5120*2+ additional*2/scale

    m = mapnik.Map(w,h)
    mapnik.load_map(m, xmlfile)

    ds = ogr.Open(borderFile)
    borderLayer = ds.GetLayer(borderFilePath)
    xStart, xEnd, yStart, yEnd = borderLayer.GetExtent()

    xStart -= additional
    yStart -= additional

    xDiff = w * scale
    yDiff = h * scale

    bbox = mapnik.Box2d(xStart, yStart, xStart + xDiff, yStart + yDiff)

    currentMinX = xStart
    currentMinY = yStart

    j = 0
    k = 0
    while (currentMinY <= yEnd):
        i = 0
        k += 1
        
        if k == threadNo:
            while (currentMinX <= xEnd):
                intersects = 0
                borderLayer.SetSpatialFilterRect(bbox.minx, bbox.miny, bbox.maxx, bbox.maxy)
                if borderLayer.GetFeatureCount() > 0:
                    intersects = 1
                    
                if intersects:  
                    m.zoom_to_box(bbox)
                    im = mapnik.Image(w, h)      
                    mapnik.render(m, im)
                    fileName = destination + str(scale) +'m_' + str(i) + '_' + str(j)
                    im.save(fileName + ".png", 'png256')
                    im = None
                    worldMapFile = worldMap(destination, i, j, scale, bbox.minx, bbox.maxy)
                    png2tiff(fileName, scale, additional, w, h)
                currentMinX = bbox.maxx - additional*2
                bbox = mapnik.Box2d(currentMinX, bbox.miny, currentMinX + xDiff, bbox.maxy)
                i += 1
        currentMinY = bbox.maxy - additional*2  
        currentMinX = xStart
        bbox = mapnik.Box2d(xStart, currentMinY, xStart + xDiff, currentMinY + yDiff)
        j += 1
        
        
def printMap(threadCount, destination, scale, xmlfile, borderFilePath):
    for i in range(1, threadCount+1):
        args = i, scale, destination, xmlfile, borderFilePath
        thread.start_new_thread(mapPrintThread, args)
      

