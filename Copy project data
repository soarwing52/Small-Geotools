import os
import shutil

project_name = raw_input('Projektname: ')
Z = 'Z:\Projekte'

path = Z +'\\' +project_name
print path

source = 'Z:\Vorlagen\Pr_Nr_Ordner_Struktur'
shutil.copytree(source,path)
print 'folder structure copied'+'\n'

bearbeitung = path +r'\5_Bearbeitung'

GIS = bearbeitung + r'\GIS'
WWK = 'Z:\Vorlagen\WWK'
shutil.copytree(WWK,GIS)

WWK_list = os.listdir(GIS)
print 'WWK copied, listed as:'+'\n'
for file in WWK_list:
    print (file)
print ' '

old_name = GIS + '\WWK_Kommune_NRW'
new_name = GIS + '\WWK_'+ project_name 
os.rename(old_name + '.mxd',new_name +'.mxd')
print 'mxd renamed'
os.rename(old_name + '.gdb',new_name +'.gdb')
print 'gdb renamed'
os.rename(old_name + '_online.mxd',new_name +'_online.mxd')
print 'mxd_online renamed'
os.rename(old_name + '_WEGEKAT_IST.mxd',new_name +'_WEGEKAT_IST.mxd')
print 'mxd_IST renamed'
os.rename(old_name + '_WEGEKAT_SOLL.mxd',new_name +'_WEGEKAT_SOLL.mxd')
print 'mxd_SOLL renamed'
raw_input('Press Enter to exit')
