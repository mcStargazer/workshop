# mesoBuffWithError.py
# Author: 
# Created: 
# Updated:


''' 
Helpful notes about the purpose, expected input, and expected output of this
script. Also a great place to store references to sources of inspiration and
algorithms used.
'''

# import modules and/or functions
import arcpy, sys, time, traceback # os

# set up a logfile
log = open('process.log','w')

try:
    ###############################################################################
    ##### environment settings
    arcpy.env.workspace = "c:/pyWork/day2/countyChaos"
    arcpy.env.overwriteOutput = True

    buffers = ["20 Kilometers", "30 Kilometers"]
    for distanceField in buffers:
        postfix = distanceField.split(' ')[0]
        ###############################################################################
        ##### geoprocessing: buffer
        # resources.arcgis.com/en/help/main/10.1/index.html#//000800000019000000
        print "Working on buffer...\n"
        inFile = "c:/pyWork/day2/countyChaos/mesonet.shp"
        outFileBuffer = "c:/pyWork/day2/countyChaos/mesonet_buffer%s.shp" % (postfix,)
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
        inFileToBeErased = "c:/pyWork/day2/countyChaos/Oklahoma.shp"
        inFileEraser = "c:/pyWork/day2/countyChaos/mesonet_buffer%s.shp" % (postfix,)
        outFileErase = "c:/pyWork/day2/countyChaos/distantLands_%skm.shp" % (postfix,)
        xyTol = "1 Meters"
        arcpy.Erase_analysis(inFileToBeErased, inFileEraser, outFileErase, xyTol)

    print "DONE!\n"

    # logfile output
    t = time.ctime()
    log.write('success message with time stamp: %s\n' % t)

except:
    # for error handling with Python, see:
    # resources.arcgis.com/en/help/main/10.1/index.html#//002z0000000q000000
    # for writing messages in script tools, see:
    # resources.arcgis.com/en/help/main/10.1/index.html#//00150000000p000000

    # collect error information from Python environment
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pyMsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + \
        str(sys.exc_info()[1]) + "\n"

    # collect error information from (and into) ArcGIS environment
    arcMsg = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    arcpy.AddError(pyMsg)
    arcpy.AddError(arcMsg)
    arcpy.AddMessage(arcpy.GetMessages(1))

    # console output
    print pyMsg
    print arcMsg
    print arcpy.GetMessages(1)

    # logfile output
    t = time.ctime()
    log.write('failure message(s) with time stamp: %s\n' % t)
    log.write(pyMsg)
    log.write(arcMsg)
    log.write(arcpy.GetMessages(1))

else: pass

finally: pass

log.close()
