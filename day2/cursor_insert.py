import arcpy

'''
NOTES:
1) You must release all locks on data before this script can run.
2) I've run this on a shapefile, and so it isn't really possible to create
   a nullable field as requested in the slide deck. Also, as the help file
   on AddField_management() states, you wind up with zeros inserted as default
   values for shapefiles. This *could* be a problem when zero actually means
   something. For instance, a temperature of 0 is a real possible temperature.
3) Try modifying it to run on a feature class and creating nullable fields if
   you want to try it on a geodatabase, too.
4) Read the online help for these arcpy members with a fine toothed comb if
   necessary. They can be persnickety.
5) Let me know if you have any troubles running this and I'll tele-help you
   to get it running.
'''

# Set environment variables
arcpy.env.workspace = "C:/pyWork/day2/countyChaos"

# Create insert cursor for table
# resources.arcgis.com/en/help/main/10.1/index.html#//018v0000002z000000
fc = "countyChaos.shp"
rows = arcpy.InsertCursor(fc)

# Weather forecast in Mordor at:
# www.collegehumor.com/picture/6689335/mordor-weather-forecast
# Create a new row and set some values to reflect the time and weather
row = rows.newRow()
row.setValue("month", "Jul")
row.setValue("day", 29)
row.setValue("year", 54)
row.setValue("temp", 133.8)
row.setValue("precip", 0.0)
row.setValue("Name", "Mordor")
rows.insertRow(row)

# Delete cursor and row objects to remove locks on the data
del row
del rows

# Add Field for walkability
# resources.arcgis.com/en/help/main/10.1/index.html#//001700000047000000
fieldName = "Walkable"
dataType = "TEXT"
fieldLength = 5                 # True and False are only expected values
 
# Execute AddField
arcpy.AddField_management(fc, fieldName, dataType, "", "", fieldLength)



