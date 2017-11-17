# ArcGIS JMeter Web Test

Tools and configuration to test peformance of ArcGIS map and feature services using Apache JMeter.


## Features

* Creates a CSV file of extents to be used as input for testing web requests using JMeter - A batch file to create extents for all scales or individual scales. Parameters required:
	* Polygon Feature Class e.g. "C:\Temp\Data\GeneralData.gdb\NewZealandLand"
	* Image DPI e.g. "96"
	* image Size e.g. "1024,768"
	* Scales e.g. "9244648.868618,4622324.434309,2311162.217155,1155581.108577,577790.554289,288895.277144,144447.638572,72223.819286,36111.909643,18055.954822,9027.977411,4513.988705,2256.994353,1128.497176,564.248588,282.124294"
	* Number of Samples e.g. "100"
	* Output CSV e.g. "C:\Temp\Data\JMeter Web Test Data.csv"
Example output [here](/Input Extents)
* [JMeter .jmx configuration files](/JMeter Configuration) to be opened and run in JMeter - Dynamic map service and feature service draw test for all or individual scales. Parameters required for Test Plan:
	* CSV Extents Path e.g. "C:\Temp\Data\JMeter Configuration"
	* Protocol DPI e.g. "https"
	* ServerName e.g. "ec2-52-64-20-102.ap-southeast-2.compute.amazonaws.com"
	* Port Number e.g. "443"
	* HTTP Request e.g. "arcgis/rest/services/MPI/NZ_Parcels_FGDB/MapServer/export?"
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


## Resources

* [GitHub](https://github.com/eaglegis)
* [Twitter](https://twitter.com/eaglegis)
* [Python for ArcGIS](http://resources.arcgis.com/en/communities/python)


## Issues

Find a bug or want to request a new feature?  Please let us know by submitting an issue.


## Contributing

Anyone and everyone is welcome to contribute. 


## Licensing
Copyright 2017 - Eagle Technology

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.