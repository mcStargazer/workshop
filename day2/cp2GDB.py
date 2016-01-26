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
# from resources.arcgis.com/en/help/main/10.1/index.html#//0017000000pw000000
# Name: CreateFileGDB_Example2.py
# Description: Create a file GDB
# Author: ESRI

# Import system modules
import arcpy

# Set local variables
out_folder_path = "C:/output" 
out_name = "fGDB.gdb"

# Execute CreateFileGDB
arcpy.CreateFileGDB_management(out_folder_path, out_name)


#---------------------------------------------------------
# from resources.arcgis.com/en/help/main/10.1/index.html#//0017000000pv000000
# Name: CreateFeaturedataset _Example2.py
# Description: Create a feature dataset 

# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = "C:/data"

# Set local variables
out_dataset_path = "C:/output/HabitatAnalysis.gdb" 
out_name = "analysisresults"
# Creating a spatial reference object
sr = arcpy.SpatialReference("C:/data/studyarea.prj")

# Create a FileGDB for the fds
arcpy.CreateFileGDB_management("C:/output", "HabitatAnalysis.gdb")

# Execute CreateFeaturedataset 
arcpy.CreateFeatureDataset_management(out_dataset_path, out_name, sr)


#---------------------------------------------------------
# from resources.arcgis.com/en/help/main/10.1/index.html#//001700000035000000
# Name: CopyFeatures_Example2.py
# Description: Convert all shapefiles in a folder to geodatabase feature classes
# Requirements: os module
# Author: ESRI
 
# Import system modules
import arcpy
from arcpy import env
import os
 
# Set environment settings
env.workspace = "C:/data"
 
# Set local variables
outWorkspace = "c:/output/output.gdb"
 
# Use ListFeatureClasses to generate a list of shapefiles in the
#  workspace shown above.
fcList = arcpy.ListFeatureClasses()
 
# Execute CopyFeatures for each input shapefile
for shapefile in fcList:
    # Determine the new output feature class path and name
    outFeatureClass = os.path.join(outWorkspace, shapefile.strip(".shp"))
    arcpy.CopyFeatures_management(shapefile, outFeatureClass)




