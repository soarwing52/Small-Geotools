# -*- coding: UTF-8 -*-
import arcpy
from arcpy.sa import *
arcpy.env.Overwrite = True

result_folder = raw_input("your result folder: ")

def main():
    ans = raw_input("do you have ndvi to calculate? (y/n) \n")
    if(ans == "y"):
        ndvi()
        main()

    elif (ans == "n"):
        raw_input("Press Enter to leave")
    else:
        print "please answer only y or n"
        main()

def ndvi():
    file = raw_input(
        "your folder of image(delete the .tar if had\n ex.D:\GIS\LC08_L1TP_118044_20161024_20170318_01_T1): \n")
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
    path = result_folder + r"\\ndvi" + name + ".tif"
    print path
    ndvi.save(path)


main()
