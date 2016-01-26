# mesoBuffer.py
# Author: 
# Created: 
# Updated:

''' 
Helpful notes and references inserted here
Ref: https://whatever.com/
'''
###############################################################################
# import 3rd party modules
import arcpy

###############################################################################
##### environment settings
arcpy.env.workspace = "c:/pyWork/countyChaos"
arcpy.env.overwriteOutput = True

buffers = ["20 Kilometers", "30 Kilometers"]
for distanceField in buffers:
    postfix = distanceField.split(' ')[0]
    ###############################################################################
    ##### geoprocessing: buffer
    # resources.arcgis.com/en/help/main/10.1/index.html#//000800000019000000
    print "Working on buffer...\n"
    inFile = "c:/pyWork/countyChaos/mesonet.shp"
    outFileBuffer = "c:/pyWork/countyChaos/mesonet_buffer%s.shp" % (postfix,)
    # distanceField = "30 Kilometers"
    sideType = "FULL"
    endType = "ROUND"
    dissolveType = "ALL"
    dissolveField = ""
    arcpy.Buffer_analysis(inFile, outFileBuffer, distanceField, sideType,
                          endType, dissolveType, dissolveField)

    ##### geoprocessing: erase
    # resources.arcgis.com/en/help/main/10.1/index.html#//00080000000m000000
    print "Working on erase...\n"
    inFileToBeErased = "c:/pyWork/countyChaos/Oklahoma.shp"
    inFileEraser = "c:/pyWork/countyChaos/mesonet_buffer%s.shp" % (postfix,)
    outFileErase = "c:/pyWork/countyChaos/distantLands_%skm.shp" % (postfix,)
    xyTol = "1 Meters"
    arcpy.Erase_analysis(inFileToBeErased, inFileEraser, outFileErase, xyTol)

print "DONE!\n"









