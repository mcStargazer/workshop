# mesoBuffWithError.py
# Author:
# Created:
# Updated:


'''
Helpful notes about the purpose, expected input, and expected output of this
script. Also a great place to store references to sources of inspiration and
algorithms used.
'''

# import standard modules
import sys
import time
import traceback

# import 3rd party modules
import arcpy

# set environment variables
arcpy.env.workspace = "c:/pyWork/day2/countyChaos"
arcpy.env.overwriteOutput = True

# set up a logfile
log = open('c:/pyWork/day2/tool_log.txt','w')

##logFile = "c:/pyWork/log_%s.txt" % (time.time(),)
##log = open(logFile,'w')

try:
    # arcpy.Clip_analysis('fruity banana goodness')
    buff1 = int(arcpy.GetParameterAsText(0))
    buff1String = "%i Kilometers" % buff1
    buff2 = int(arcpy.GetParameterAsText(1))
    buff2String = "%i Kilometers" % buff2
    buffers = [buff1String, buff2String]
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
        arcpy.Buffer_analysis(inFile, outFileBuffer, distanceField, sideType, endType, dissolveType, dissolveField)

        ##### geoprocessing: erase
        # resources.arcgis.com/en/help/main/10.1/index.html#//00080000000m000000
        print "Working on erase...\n"
        inFileToBeErased = "c:/pyWork/day2/countyChaos/Oklahoma.shp"
        inFileEraser = "c:/pyWork/day2/countyChaos/mesonet_buffer%s.shp" % (postfix,)
        outFileErase = "c:/pyWork/day2/countyChaos/distantLands_%skm.shp" % (postfix,)
        xyTol = "1 Meters"
        arcpy.Erase_analysis(inFileToBeErased, inFileEraser, outFileErase, xyTol)

    # logfile output
    t = time.ctime()
    log.write( 'success on %s\n' % (t,) )

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
    log.write( 'failure at %s\n' % (t,) )
    log.write(pyMsg)
    log.write(arcMsg)
    log.write(arcpy.GetMessages(1))

else: pass

finally: pass

log.close()
