# Name: ExtactFeaturesByLocationAndAttribute.py
# Description: Extract features to a new feature class based
# on a spatial relationships to another layer AND an attribute
# query
 
# Import system modules
import arcpy

# Set the environment variables
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "c:/pyWork/day2/fGDB.gdb/mesonet"

# Make a layer from the feature class
arcpy.MakeFeatureLayer_management("mesonet", "lyr") 

# select mesonet stations with name like 'C%'
sql = "\"NAME\" LIKE 'C%'"
arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", sql)
 
# Write the selected features to a new featureclass
arcpy.CopyFeatures_management("lyr", "chihuahua_10000plus")
