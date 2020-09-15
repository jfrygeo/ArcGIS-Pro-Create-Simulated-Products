# Name: TableToTable.py
# Description: Export table
# Requirements: os module

# Import system modules
import arcpy
import os

#parameters
inRows = arcpy.GetParameterAsText(0)
outPath = arcpy.GetParameterAsText(1)
outName = arcpy.GetParameterAsText(2)



# Create a new fieldmappings
fieldmappings = arcpy.FieldMappings()
fieldmappings.addTable(inRows)
#fieldmappings.addTable(out)

 
#Run the TableToTable tool
arcpy.TableToTable_conversion(in_rows=inRows, out_path=outPath, out_name=outName, where_clause=None, field_mapping=fieldmappings, config_keyword=None)
arcpy.SetParameter(3, os.path.join(outPath,outName))
arcpy.FieldMappings.removeAll(fieldmappings)
