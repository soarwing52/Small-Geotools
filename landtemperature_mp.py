# -*- coding: UTF-8 -*-
import os
from multiprocessing import Pool
import arcpy
from arcpy.sa import Divide, Float, Raster, Ln

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'D:\Small-Geotools'

RESULT_FOLDER = 'D:\\surface'
TARGET_FOLDER = r'F:\\landsat 2020'

RADIANCE_MULT_BAND = 0.0003342
RADIANCE_ADD = 0.1
Oi = 0.29
K1_CONSTANT_BAND_10 = 774.8853
K2_CONSTANT_BAND_10 = 1321.0789

def mp_land_temperature(file):
    path_thermal = file + "\\" + file[-40:] + "_B10.tif"
    location = file[-30:-24]
    date = file[-24:-15]
    name = date + "_" + location
    print(name)

    arcpy.env.scratchWorkspace = os.path.join(arcpy.env.workspace, name)  # r'C:\Users\yourname\PSU_LiDAR\f'+raster.replace(".img","") 

    if not os.path.exists(arcpy.env.scratchWorkspace): 
        os.makedirs(arcpy.env.scratchWorkspace)        

        path_thermal = file + "\\" + file[-40:] + "_B10.tif"

    thermal_band = Raster(path_thermal)
    print thermal_band
    print "band condirmed"

    Rfloat = Float(thermal_band)
    top_temperature = Rfloat * RADIANCE_MULT_BAND + RADIANCE_ADD - Oi
    temp_tif = "temp{}.tif".format(name)
    top_temperature.save(temp_tif)

    top_temperature = Raster(temp_tif)
    top_temperature = Float(top_temperature)

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

if __name__ == '__main__':
    print("GO")

    target_list = []
    for x in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, x)
        if os.path.isdir(file_path):
            print(file_path)
            target_list.append(file_path)

    pool = Pool()
    pool.map(mp_land_temperature,target_list)   
