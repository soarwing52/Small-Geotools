import arcpy
arcpy.env.overwriteOutput = True
folder = raw_input("link of folder: ")
print folder
new = folder.replace("\\","\\\\")
new = new.replace(r"\\",r"/")

arcpy.env.workplace = folder
arcpy.CreateFileGDB_management(folder,"Luftbild.gdb","10.0")
print "gdb sucess"        
geodatabase = new + "/Luftbild.gdb"
arcpy.CreateRasterCatalog_management(geodatabase,"raslog","","","","","","","UNMANAGED","")
print "raslog complete"

raslog = geodatabase + "/raslog"

arcpy.WorkspaceToRasterCatalog_management(folder, raslog ,"INCLUDE_SUBDIRECTORIES","NONE")
print "imported"

raw_input("Press enter to exit")
