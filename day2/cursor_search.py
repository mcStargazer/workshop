import arcpy

LUT={"JAN":1,"FEB":2,"MAR":3,"APR":4,"MAY":5,"JUN":6,"JUL":7,"AUG":8,"SEP":9,"OCT":10,"NOV":11,"DEC":12}
outFile = open('c:/pyWork/badMonths.csv','w')

arcpy.env.workspace = "c:/pyWork/countyChaos"
fc = "countyChaos.shp"
field = "month"
cursorS = arcpy.SearchCursor(fc,"","","","")
for row in cursorS:
    month = row.getValue(field)
    try:
        mm = LUT[ month[:3].upper()]
    except:
        # write out to a CSV file if not found in LUT
        outFile.write('%s,%s\n' % (row.getValue("FID"), month) )
outFile.close()
