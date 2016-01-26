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
import arcpy, sys, traceback # os, time

# set up a logfile
#log = open('','w')

try:
	# environment settings


	# input files


	# output files


	# geoprocessing logic
	# http://resources.arcgis.com/en/help/previous-help/index.html
        arcpy.Clip_analysis('fruity banana goodness')

	# logfile output
	# t = time.ctime()
	#log.write('success message with time stamp\n')

except: pass
##      # for error handling with Python, see:
##      # resources.arcgis.com/en/help/main/10.1/index.html#//002z0000000q000000
##      # for writing messages in script tools, see:
##      # resources.arcgis.com/en/help/main/10.1/index.html#//00150000000p000000
##
##      # collect error information from Python environment
##	tb = sys.exc_info()[2]
##	tbinfo = traceback.format_tb(tb)[0]
##	pyMsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n" + \
##		str(sys.exc_info()[1]) + "\n"
##
##      # collect error information from (and into) ArcGIS environment
##	arcMsg = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"
##	arcpy.AddError(pyMsg)
##	arcpy.AddError(arcMsg)
##	arcpy.AddMessage(arcpy.GetMessages(1))
##
##	# console output
##	print pyMsg
##	print arcMsg
##	print arcpy.GetMessages(1)
##
##	# logfile output
##	# t = time.ctime()
##	# log.write('failure message(s) with time stamp\n')

else: pass

finally: pass

#log.close()
