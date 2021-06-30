# -*- coding: UTF-8 -*-
import os
import arcpy
from arcpy.sa import *
import random

arcpy.env.Overwrite = True
arcpy.env.scratchWorkspace = os.path.dirname(__file__)
RESULT_FOLDER = 'D:\\surface'
TARGET_FOLDER = r'F:\\landsat 2020'


def land_surface_temp(file, i):
    arcpy.env.Overwrite = True
    # file = raw_input(
    #     "your folder of image(delete the .tar if had\n ex.D:\GIS\LC08_L1TP_118044_20161024_20170318_01_T1): \n")
    path_thermal = file + "\\" + file[-40:] + "_B10.tif"

    RADIANCE_MULT_BAND = 0.0003342
    RADIANCE_ADD = 0.1
    Oi = 0.29

    thermal_band = Raster(path_thermal)
    print thermal_band
    print "band condirmed"

    Rfloat = Float(thermal_band)
    top_temperature = Rfloat * RADIANCE_MULT_BAND + RADIANCE_ADD - Oi
    temp_tif = "temp{}.tif".format(i)
    #temp_tif = "temp.tif"
    top_temperature.save(temp_tif)

    top_temperature = Raster(temp_tif)
    top_temperature = Float(top_temperature)

    K1_CONSTANT_BAND_10 = 774.8853
    K2_CONSTANT_BAND_10 = 1321.0789

    divide1 = Divide(K1_CONSTANT_BAND_10 , (top_temperature + 1))
    ln1 = Ln(divide1)
    surface_temp = Divide(K2_CONSTANT_BAND_10, ln1) - 273.15    

    location = file[-30:-24]
    date = file[-24:-15]
    name = date + "_" + location
    print name
    path = "surface_temp" + name + ".tif"
    print path
    surface_temp.save(path)
    i += 1

if __name__ == '__main__':
    print("GO")
    arcpy.env.Overwrite = True
    i = 1
    for x in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, x)
        if os.path.isdir(file_path):
            print(file_path)
            land_surface_temp(file_path, i)
            i += 1
