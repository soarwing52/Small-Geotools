# -*- coding: UTF-8 -*-
import os
import arcpy
from arcpy.sa import *
arcpy.env.Overwrite = True
arcpy.env.scratchWorkspace = os.path.dirname(r"D:\temp")

RESULT_FOLDER = r'D:\NDVI_R'
TARGET_FOLDER = r'D:\NDVI'

def ndvi(dir):
    # file = raw_input(
    #     "your folder of image(delete the .tar if had\n ex.D:\GIS\LC08_L1TP_118044_20161024_20170318_01_T1): \n")

    path_red = dir + "\\" + dir[-40:] + "_B4.tif"
    path_nir = dir + "\\" + dir[-40:] + "_B5.tif"

    red_band_raster = Raster(path_red)
    nir_band_raster = Raster(path_nir)
    print red_band_raster
    print nir_band_raster
    print "band condirmed"

    Rfloat = Float(red_band_raster)
    Nfloat = Float(nir_band_raster)
    ndvi = Divide((Nfloat - Rfloat), (Nfloat + Rfloat))
    location = dir[-30:-24]
    date = dir[-24:-15]
    name = date + "_" + location
    print name
    path = RESULT_FOLDER + r"\\ndvi_" + name + ".tif"
    print path
    ndvi.save(path)

def new_ndvi(dir):
    files = os.listdir(dir)
    # print files
    b4,b5="",""
    for file in files:
        if "_B4" in file:
            b4 = file
        elif "_B5" in file:
            b5 = file

    path_red = dir + "\\" + b4
    path_nir = dir + "\\" + b5

    print b4,b5

    red_band_raster = Raster(path_red)
    nir_band_raster = Raster(path_nir)
    print red_band_raster
    print nir_band_raster
    print "band condirmed"
    
    Rfloat = Float(red_band_raster)
    Rfloat.save("Rfloat.tif")
    Nfloat = Float(nir_band_raster)
    Nfloat.save("Nfloat.tif")
    ndvi = Divide((Nfloat - Rfloat), (Nfloat + Rfloat))
    ndvi.save("ndvi.tif")

if __name__ == '__main__':
    print("GO")
    for x in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, x)
        if os.path.isdir(file_path):
            print(file_path)
            new_ndvi(file_path)
