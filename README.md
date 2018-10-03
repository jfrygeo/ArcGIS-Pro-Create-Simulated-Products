# ArcGIS-Pro-Create-Simulated-Products
ArcGIS Pro project that contains a tool that allows a user to create a csv output to be used as simulation file for ArcGIS GeoEvent Server. The tool takes a user edited track and a defined speed of a platform and creates points along the track line in a distance defined by the time of 1 sec. For instance, if a vessel is travelling 60 km/hr the line will have a point every 16.667 meters. When these points will be in the simulator (at 1 second updates), an updated will show the position 16.67 meters away. The tool also calculates the heading of the points along the line. 

## Usage
A user can open the [CreateSimulatedProducts ArcGIS Pro Package](https://github.com/jfrygeo/ArcGIS-Pro-Create-Simulated-Products/tree/master/Pro%20Package) to utilize the tool. 
The map opens with some example data of track polylines and points. 

![Map](https://github.com/jfrygeo/ArcGIS-Pro-Create-Simulated-Products/blob/master/Screencaptures/FinalOutput.PNG "Map")

A user can delete the features in the "Tracks", manually or by running a tool like [delete rows](http://pro.arcgis.com/en/pro-app/tool-reference/data-management/delete-rows.htm). The user can create new features by selecting "Create Features" and then begin to create tracks of different platform types. Make sure to edit the attribute data and specify a <b>Speed</b> (in km/hr) and a <b>Platform Name </b>. The <b>Platform Name</b> works as a track id and is very important. 

The image below shows some example tracks and the create features tab.

![Create Features](https://github.com/jfrygeo/ArcGIS-Pro-Create-Simulated-Products/blob/master/Screencaptures/CreateTracksEditAttributeData.PNG "Create Features")

Once a user creates the tracks the user must save the edits. Now the user can run the <b>Create Simulated Points for GeoEvent<b> tool. The tool allows the user to specify the tracks (in which the user edited above), an output folder, and a name for the CSV file. 
  
![Create Features](https://github.com/jfrygeo/ArcGIS-Pro-Create-Simulated-Products/blob/master/Screencaptures/CreateSimulatedPointsForGeoEventGUI.PNG "Create Features")
  
The tool will take some time if you have a long track. When the tool executes, it will export a feature class of all the points, and a CSV of the points. The csv can be used in the [GeoEvent Simulator](http://enterprise.arcgis.com/en/geoevent/latest/administer/geoevent-simulator.htm). The updates in the simulator will passed to GeoEvent over Text over TCP Connection. When a GeoEvent Input retrives the positions in the simulator, you can create an output to update a feature service with new positions. 

The image below shows the positions being updated in a web map.

![Web Map](https://github.com/jfrygeo/ArcGIS-Pro-Create-Simulated-Products/blob/master/Screencaptures/WebMapFeatures.PNG "Web Map")
