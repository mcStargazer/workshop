import arcpy

'''
NOTES:
1) Once again, make sure there are no file locks when this is run. If you
   have to, close down ArcProducts and/or the Python shell (not the editor),
   then restart them after running this stand-alone script.
2) Let me know if you have any troubles running this and I'll tele-help you
   to get it running.
'''

# Set environment variables
arcpy.env.workspace = "C:/pyWork/day2/countyChaos"

# Update the "Walkable" field in the countyChaos shapefile
# resources.arcgis.com/en/help/main/10.1/index.html#//018v00000064000000
fc = "countyChaos.shp"
fieldName = "Walkable"

uCur = arcpy.UpdateCursor(fc,"","","","")
for row in uCur:
    print row.getValue("temp")
    if row.getValue("Name") == "Mordor":
        row.setValue(fieldName, "False")
    else:
        row.setValue(fieldName, "True")
    uCur.updateRow(row)

del uCur
del row
