# -*- coding: UTF-8 -*-
import os
import arcpy
from arcpy.sa import *
arcpy.env.Overwrite = True

RESULT_FOLDER = 'D:\\NDVI_R'
TARGET_FOLDER = r'D:\ndvi\Bulk Order ndvi\Landsat 8 OLI_TIRS C2 L1'

def ndvi(file):
    # file = raw_input(
    #     "your folder of image(delete the .tar if had\n ex.D:\GIS\LC08_L1TP_118044_20161024_20170318_01_T1): \n")
    path_red = file + "\\" + file[-40:] + "_B4.tif"
    path_nir = file + "\\" + file[-40:] + "_B5.tif"

    red_band_raster = Raster(path_red)
    nir_band_raster = Raster(path_nir)
    print red_band_raster
    print nir_band_raster
    print "band condirmed"

    Rfloat = Float(red_band_raster)
    Nfloat = Float(nir_band_raster)
    ndvi = Divide((Nfloat - Rfloat), (Nfloat + Rfloat))
    location = file[-30:-24]
    date = file[-24:-15]
    name = date + "_" + location
    print name
    path = RESULT_FOLDER + r"\\ndvi_" + name + ".tif"
    print path
    ndvi.save(path)

if __name__ == '__main__':
    print("GO")
    for x in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, x)
        if os.path.isdir(file_path):
            print(file_path)
            ndvi(file_path)
