# -*- coding: UTF-8 -*-
import os
from multiprocessing import Pool, Process
from arcpy import env
from arcpy.sa import Raster,Float, Divide, Ln, Square, Minus
from arcpy import GetRasterProperties_management, CreateFileGDB_management

def create_dir(name="workspace.gdb"):
    try:
        dir = os.getcwd()
        CreateFileGDB_management(dir,name)
    except WindowsError:
        pass
    finally:
        return os.path.abspath(name)

def calculate_LST(source_dir):
    dir_name = os.path.dirname(source_dir)
    basename = os.path.basename(source_dir)
    print (dir_name, basename)
    workspace = create_dir(basename + ".gdb")
    print workspace
    env.workspace = workspace
    env.overwriteOutput = True
    Band4 = "{}/{}_B4.tif".format(source_dir, basename)
    Band5 = "{}/{}_B5.tif".format(source_dir, basename)
    Band10 = "{}/{}_B10.tif".format(source_dir, basename)

    Band4_R = Raster(Band4)
    Band5_R = Raster(Band5)
    Band5_R.save("{}/{}_bands".format(workspace,basename))

    Band4 = Float(Band4_R)
    Band5 = Float(Band5_R)
    Band10 = Float(Raster(Band10))

    NDVI = Divide((Band5 - Band4), (Band5 + Band4))
    NDVI_path = "{}/{}_ndvi".format(workspace,basename)
    print NDVI_path
    NDVI.save(NDVI_path)

    NDVI_max = GetRasterProperties_management(NDVI_path, property_type="MAXIMUM").getOutput(0)
    NDVI_min = GetRasterProperties_management(NDVI_path, property_type="MINIMUM").getOutput(0)
    a = Minus(NDVI, -1)
    b = float(NDVI_max) - float(NDVI_min)
    c = Divide(a, b)
    PV = Square(c)
    E = 0.004 * PV + 0.986
    E.save("{}/{}_E".format(workspace,basename))

    TOA = 0.0003342 * Band10 + 0.1
    BT = 1321.08 / Ln((774.89 / TOA) + 1) - 273.15
    d = 1 + (0.00115 * BT / 1.4388) + Ln(E)
    LST = Divide(BT, d)
    print LST, type(LST)
    LST_Path = "{}/{}_LST".format(workspace,basename)
    LST.save(LST_Path)
    print (LST_Path)


if __name__ == '__main__':
    dirname = "2018"
    #calculate_LST(r"D:\surface_temp\LC08_L1TP_118044_20181030_20181115_01_T1")
    img_list = ["D:\surface_temp/2018/" + img for img in os.listdir(dirname) if os.path.isdir("2018/" + img)]
    print img_list
    for file in img_list:
        pro = Process(target=calculate_LST, args=img)
        pro.start()
        print "start"