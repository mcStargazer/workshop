# cp2GDB.py
# Author: 
# Created: 
# Updated:


''' 
Helpful notes about the purpose, expected input, and expected output of this
script. Also a great place to store references to sources of inspiration and
algorithms used.
'''

#---------------------------------------------------------

# Name: CreateFileGDB_Example2.py
# Description: Create a file GDB
# Author: ESRI

# Import system modules
import arcpy
import os

# Set local variables
out_folder_path = "C:/pyWork/day2" 
out_gdb_name = "fGDB.gdb"
arcpy.env.workspace = "C:/pyWork/day2/countyChaos"
arcpy.env.overwriteOutput = True

# Execute CreateFileGDB
# from resources.arcgis.com/en/help/main/10.1/index.html#//0017000000pw000000
arcpy.CreateFileGDB_management(out_folder_path, out_gdb_name)

# Set local variables
out_dataset_path = out_folder_path + "/" + out_gdb_name 
out_fd_name = "mesonet"
# Creating a spatial reference object
sr = arcpy.SpatialReference("C:/pyWork/day2/countyChaos/mesonet.prj")

# Execute CreateFeaturedataset
# from resources.arcgis.com/en/help/main/10.1/index.html#//0017000000pv000000
arcpy.CreateFeatureDataset_management(out_dataset_path, out_fd_name, sr)

# Use ListFeatureClasses to generate a list of shapefiles in the
#  workspace shown above.
fcList = arcpy.ListFeatureClasses()
 
# Execute CopyFeatures for each input shapefile
for shapefile in fcList:
    # Determine the new output feature class path and name
    out_dataset_path = out_folder_path + "/" + out_gdb_name + \
                        "/" + out_fd_name
    outFeatureClass = out_dataset_path + "/" + shapefile.split(".")[0]
    # resources.arcgis.com/en/help/main/10.1/index.html#//001700000035000000
    arcpy.CopyFeatures_management(shapefile, outFeatureClass)




