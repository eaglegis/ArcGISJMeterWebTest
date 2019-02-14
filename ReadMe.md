# ArcGIS JMeter Web Test

Tools and configuration to test peformance of ArcGIS map and feature services using Apache JMeter.


## Features

* Creates a CSV file of extents to be used as input for testing web requests using JMeter - A batch file to create extents for all scales or individual scales. Parameters required:
	* Polygon feature class of the extent to create test data for e.g. "C:\Temp\Data\GeneralData.gdb\NewZealandLand"
	* Image DPI for all requests e.g. "96"
	* Image size (width and height) for all requests e.g. "1024,768"
	* Scales to use in requests e.g. "4513.988705,2256.994353,1128.497176,564.248588" or "4513.988705" for just one scsale
	* Service URLs to use in request. Can be map service, map service layer or feature service. Do not put protocol. e.g. "services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/New_Zealand_Schools/FeatureServer/0,services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/NZ_Base_Data_Fire_Station_Locations_2008/FeatureServer/0"
	* URL to portal site
	* Portal user that has access to the services
	* Portal user password
	* Number of samples to create e.g. "100"
	* Location of output CSV to be created e.g. "%~dp0\Input Extents\Extents - New Zealand Land (NZTM).csv"
Example output [here](/Input Extents)
* [JMeter .jmx configuration files](/JMeter Configuration) to be opened and run in JMeter - Dynamic map service and feature service draw test for all or individual scales.
* Creates a report table showing the draw times for a particular service.


## Requirements

* [Apache JMeter](http://jmeter.apache.org)
* Internet access
* ArcGIS Desktop 10.1/Python 2.7+


## Installations Instructions

* Install ArcMap on machine along with Python 2.7.
* Fork/clone the repository or download the .zip file.
* Edit the "Create JMeter Web Test Extents" batch files and set the necessary parameters.
* Run the "Create JMeter Web Test Extents" batch files to create CSV files for input to JMeter.
* Download and run Apache JMeter.
* Open one of the [JMeter .jmx configuration files](/JMeter Configuration)
* Set the input parameters for the test plan.
* Run the test plan.