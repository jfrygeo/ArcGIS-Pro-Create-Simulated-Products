# Name: SpatialJoin.py
# Description: Join attributes the lines and point datasets
# Requirements: os module

# Import system modules
import arcpy
import os

#parameters
targetFeatures = arcpy.GetParameterAsText(0)
joinFeatures = arcpy.GetParameterAsText(1)
search_radius = arcpy.GetParameterAsText(2)
outfc = arcpy.GetParameterAsText(3)


# Create a new fieldmappings and add the two input feature classes.
fieldmappings = arcpy.FieldMappings()
fieldmappings.addTable(targetFeatures)
fieldmappings.addTable(joinFeatures)

 
#Run the Spatial Join tool, using the defaults for the join operation and join type
arcpy.SpatialJoin_analysis(targetFeatures, joinFeatures, outfc, "JOIN_ONE_TO_ONE", "KEEP_ALL", fieldmappings, "INTERSECT", search_radius)
arcpy.FieldMappings.removeAll(fieldmappings)