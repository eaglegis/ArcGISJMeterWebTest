:::::::::::::::::::::::::::::::::::::::::::::::::::: PARAMETERS ::::::::::::::::::::::::::::::::::::::::::::::::::::
:: ----- Python install location
SET PYTHON_LOCATION="C:\Python27\ArcGIS10.6\python"
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: ----- Create JMeter Web Test Extents -----
:: Parameters:
:: 	Polygon feature class of the extent to create test data for e.g. "C:\Temp\Data\GeneralData.gdb\NewZealandLand"
:: 	Image DPI for all requests e.g. "96"
:: 	Image size (width and height) for all requests e.g. "1024,768"
::	Scales to use in requests e.g. "4513.988705,2256.994353,1128.497176,564.248588" or "4513.988705" for just one scsale
::	Service URLs to use in request. Can be map service, map service layer or feature service. Do not put protocol. e.g. "services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/New_Zealand_Schools/FeatureServer/0,services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/NZ_Base_Data_Fire_Station_Locations_2008/FeatureServer/0"
::	URL to portal site
:: 	Portal user that has access to the services
::	Portal user password
::	Number of samples to create e.g. "100"
::	Location of output CSV to be created e.g. "%~dp0\Input Extents\Extents - New Zealand Land (NZTM).csv"
%PYTHON_LOCATION% "%~dp0\CreateJMeterWebTestData.py" ^
 "C:\Temp\Data\GeneralData.gdb\NewZealandLand" ^
 "96" ^
 "1024,768" ^
 "36111.909643" ^
 "services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/New_Zealand_Schools/FeatureServer/0,services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/NZ_Base_Data_Fire_Station_Locations_2008/FeatureServer/0" ^
 "" ^
 "" ^
 "" ^
 "10" ^
 "%~dp0\Input Data\Extents at 36111 - New Zealand Land (NZTM).csv"

%PYTHON_LOCATION% "%~dp0\CreateJMeterWebTestData.py" ^
 "C:\Temp\Data\GeneralData.gdb\NewZealandLand" ^
 "96" ^
 "1024,768" ^
 "18055.954822" ^
 "services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/New_Zealand_Schools/FeatureServer/0,services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/NZ_Base_Data_Fire_Station_Locations_2008/FeatureServer/0" ^
 "" ^
 "" ^
 "" ^
 "10" ^
 "%~dp0\Input Data\Extents at 18055 - New Zealand Land (NZTM).csv"

%PYTHON_LOCATION% "%~dp0\CreateJMeterWebTestData.py" ^
 "C:\Temp\Data\GeneralData.gdb\NewZealandLand" ^
 "96" ^
 "1024,768" ^
 "9027.977411" ^
 "services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/New_Zealand_Schools/FeatureServer/0,services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/NZ_Base_Data_Fire_Station_Locations_2008/FeatureServer/0" ^
 "" ^
 "" ^
 "" ^
 "10" ^
 "%~dp0\Input Data\Extents at 9027 - New Zealand Land (NZTM).csv"

%PYTHON_LOCATION% "%~dp0\CreateJMeterWebTestData.py" ^
 "C:\Temp\Data\GeneralData.gdb\NewZealandLand" ^
 "96" ^
 "1024,768" ^
 "4513.988705" ^
 "services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/New_Zealand_Schools/FeatureServer/0,services.arcgis.com/XTtANUDT8Va4DLwI/arcgis/rest/services/NZ_Base_Data_Fire_Station_Locations_2008/FeatureServer/0" ^
 "" ^
 "" ^
 "" ^
 "10" ^
 "%~dp0\Input Data\Extents at 4513 - New Zealand Land (NZTM).csv"