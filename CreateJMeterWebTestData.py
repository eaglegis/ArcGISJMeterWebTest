#-------------------------------------------------------------
# Name:       Create JMeter Web Test Data
# Purpose:    Creates a CSV file of extents to be used as input for testing
#             web requests using JMeter.
# Author:     Shaun Weston (shaun_weston@eagle.co.nz)
# Date Created:    10/11/2017
# Last Updated:    11/11/2017
# Copyright:   (c) Eagle Technology
# ArcGIS Version:   ArcMap 10.1+
# Python Version:   2.7+
#--------------------------------

# Import main modules
import os
import sys
import logging
import smtplib

# Set global variables
# Logging
enableLogging = "false" # Use within code - logger.info("Example..."), logger.warning("Example..."), logger.error("Example...") and to print messages - printMessage("xxx","info"), printMessage("xxx","warning"), printMessage("xxx","error")
logFile = "" # e.g. os.path.join(os.path.dirname(__file__), "Example.log")
# Email logging
sendErrorEmail = "false"
emailServerName = "" # e.g. smtp.gmail.com
emailServerPort = 0 # e.g. 25
emailTo = ""
emailUser = ""
emailPassword = ""
emailSubject = ""
emailMessage = ""
# Proxy
enableProxy = "false"
requestProtocol = "http" # http or https
proxyURL = ""
# Output
output = None
# ArcGIS desktop installed
arcgisDesktop = "true"

# If ArcGIS desktop installed
if (arcgisDesktop == "true"):
    # Import extra modules
    import arcpy
    # Enable data to be overwritten
    arcpy.env.overwriteOutput = True
# Python version check
if sys.version_info[0] >= 3:
    # Python 3.x
    import urllib.request as urllib2
else:
    # Python 2.x
    import urllib2
import csv
import random


# Start of main function
def mainFunction(polygonFeatureClass,imageDPI,imageSize,scales,numberOfSamples,outputCSV): # Get parameters from ArcGIS Desktop tool by seperating by comma e.g. (var1 is 1st parameter,var2 is 2nd parameter,var3 is 3rd parameter)
    try:
        # --------------------------------------- Start of code --------------------------------------- #
        # Generate random points and add coordinates
        printMessage("Creating random points within specified extent - " + os.path.join(arcpy.env.scratchGDB, "SamplePoints") + "...","info")
        arcpy.CreateRandomPoints_management(arcpy.env.scratchGDB, "SamplePoints", polygonFeatureClass, "0 0 0 0", numberOfSamples, "0 Unknown", "POINT", "0")
        arcpy.AddXY_management(os.path.join(arcpy.env.scratchGDB, "SamplePoints"))
        arcpy.AddField_management(os.path.join(arcpy.env.scratchGDB, "SamplePoints"), "XMin", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(os.path.join(arcpy.env.scratchGDB, "SamplePoints"), "YMin", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(os.path.join(arcpy.env.scratchGDB, "SamplePoints"), "XMax", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(os.path.join(arcpy.env.scratchGDB, "SamplePoints"), "YMax", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(os.path.join(arcpy.env.scratchGDB, "SamplePoints"), "Scale", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(os.path.join(arcpy.env.scratchGDB, "SamplePoints"), "MaxAllowableOffset", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Get the image width and height
        imageSize = imageSize.split(',')

        # Get the scales
        scales = scales.split(',')

        # Go through each point in the feature class
        printMessage("Calculating extent for each point" + "...","info")
        with arcpy.da.UpdateCursor(os.path.join(arcpy.env.scratchGDB, "SamplePoints"), ["POINT_X","POINT_Y","XMin","YMin","XMax","YMax","Scale","MaxAllowableOffset"]) as updateCursor:
            # For each row in the table
            for row in updateCursor:
                # Randomly pick a scale from the list
                scale = random.choice(scales)
                # Get the map height and width for the image size and scale
                mapWidthHalf =  (((float(imageSize[0])/float(imageDPI)) * 0.0254) * float(scale)) / 2
                mapHeightHalf =  (((float(imageSize[1])/float(imageDPI)) * 0.0254) * float(scale)) / 2

                # Get the max allowable offset for feature services
                maxAllowableOffset = (((float(imageSize[0])/float(imageDPI)) * 0.0254) * float(scale)) / float(imageSize[0])

                # Create the extent for the point based on the calculation above
                row[2] = row[0] - mapWidthHalf
                row[3] = row[1] - mapHeightHalf
                row[4] = row[0] + mapWidthHalf
                row[5] = row[1] + mapHeightHalf
                row[6] = scale
                row[7] = maxAllowableOffset
                updateCursor.updateRow(row)

        # Create a CSV file and setup header
        file = open(outputCSV, 'wb')
        writer = csv.writer(file, delimiter=",")

        # Add in header information
        headerRow = []
        headerRow.append("X")
        headerRow.append("Y")
        headerRow.append("XMin")
        headerRow.append("YMin")
        headerRow.append("XMax")
        headerRow.append("YMax")
        headerRow.append("Scale")
        headerRow.append("MaxAllowableOffset")
        writer.writerow(headerRow)

        # Write in each of the values for all of the records
        printMessage("Creating the CSV File - " + outputCSV + "...","info")
        with arcpy.da.SearchCursor(os.path.join(arcpy.env.scratchGDB, "SamplePoints"), ["POINT_X","POINT_Y","XMin","YMin","XMax","YMax","Scale","MaxAllowableOffset"]) as searchCursor:
            # For each row in the table
            for row in searchCursor:
                # For each value in the row
                values = []
                for value in row:
                    values.append(value)
                # Write the row to the CSV file
                writer.writerow(values)

        # --------------------------------------- End of code --------------------------------------- #
        # If called from gp tool return the arcpy parameter
        if __name__ == '__main__':
            # Return the output if there is any
            if output:
                # If ArcGIS desktop installed
                if (arcgisDesktop == "true"):
                    arcpy.SetParameter(1, output)
                # ArcGIS desktop not installed
                else:
                    return output
        # Otherwise return the result
        else:
            # Return the output if there is any
            if output:
                return output
        # Logging
        if (enableLogging == "true"):
            # Log end of process
            logger.info("Process ended.")
            # Remove file handler and close log file
            logMessage.flush()
            logMessage.close()
            logger.handlers = []
    # If arcpy error
    except arcpy.ExecuteError:
        # Build and show the error message
        errorMessage = arcpy.GetMessages(2)
        printMessage(errorMessage,"error")
        # Logging
        if (enableLogging == "true"):
            # Log error
            logger.error(errorMessage)
            # Log end of process
            logger.info("Process ended.")
            # Remove file handler and close log file
            logMessage.flush()
            logMessage.close()
            logger.handlers = []
        if (sendErrorEmail == "true"):
            # Send email
            sendEmail(errorMessage)
    # If python error
    except Exception as e:
        errorMessage = ""
        # Build and show the error message
        # If many arguments
        if (e.args):
            for i in range(len(e.args)):
                if (i == 0):
                    # Python version check
                    if sys.version_info[0] >= 3:
                        # Python 3.x
                        errorMessage = str(e.args[i]).encode('utf-8').decode('utf-8')
                    else:
                        # Python 2.x
                        errorMessage = unicode(e.args[i]).encode('utf-8')
                else:
                    # Python version check
                    if sys.version_info[0] >= 3:
                        # Python 3.x
                        errorMessage = errorMessage + " " + str(e.args[i]).encode('utf-8').decode('utf-8')
                    else:
                        # Python 2.x
                        errorMessage = errorMessage + " " + unicode(e.args[i]).encode('utf-8')
        # Else just one argument
        else:
            errorMessage = e
        printMessage(errorMessage,"error")
        # Logging
        if (enableLogging == "true"):
            # Log error
            logger.error(errorMessage)
            # Log end of process
            logger.info("Process ended.")
            # Remove file handler and close log file
            logMessage.flush()
            logMessage.close()
            logger.handlers = []
        if (sendErrorEmail == "true"):
            # Send email
            sendEmail(errorMessage)
# End of main function


# Start of print message function
def printMessage(message,type):
    # If ArcGIS desktop installed
    if (arcgisDesktop == "true"):
        if (type.lower() == "warning"):
            arcpy.AddWarning(message)
        elif (type.lower() == "error"):
            arcpy.AddError(message)
        else:
            arcpy.AddMessage(message)
    # ArcGIS desktop not installed
    else:
        print(message)
# End of print message function


# Start of set logging function
def setLogging(logFile):
    # Create a logger
    logger = logging.getLogger(os.path.basename(__file__))
    logger.setLevel(logging.DEBUG)
    # Setup log message handler
    logMessage = logging.FileHandler(logFile)
    # Setup the log formatting
    logFormat = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s", "%d/%m/%Y - %H:%M:%S")
    # Add formatter to log message handler
    logMessage.setFormatter(logFormat)
    # Add log message handler to logger
    logger.addHandler(logMessage)

    return logger, logMessage
# End of set logging function


# Start of send email function
def sendEmail(message):
    # Send an email
    printMessage("Sending email...","info")
    # Server and port information
    smtpServer = smtplib.SMTP(emailServerName,emailServerPort)
    smtpServer.ehlo()
    smtpServer.starttls()
    smtpServer.ehlo
    # Login with sender email address and password
    smtpServer.login(emailUser, emailPassword)
    # Email content
    header = 'To:' + emailTo + '\n' + 'From: ' + emailUser + '\n' + 'Subject:' + emailSubject + '\n'
    body = header + '\n' + emailMessage + '\n' + '\n' + message
    # Send the email and close the connection
    smtpServer.sendmail(emailUser, emailTo, body)
# End of send email function


# This test allows the script to be used from the operating
# system command prompt (stand-alone), in a Python IDE,
# as a geoprocessing script tool, or as a module imported in
# another script
if __name__ == '__main__':
    # Test to see if ArcGIS desktop installed
    if ((os.path.basename(sys.executable).lower() == "arcgispro.exe") or (os.path.basename(sys.executable).lower() == "arcmap.exe") or (os.path.basename(sys.executable).lower() == "arccatalog.exe")):
        arcgisDesktop = "true"

    # If ArcGIS desktop installed
    if (arcgisDesktop == "true"):
        argv = tuple(arcpy.GetParameterAsText(i)
            for i in range(arcpy.GetArgumentCount()))
    # ArcGIS desktop not installed
    else:
        argv = sys.argv
        # Delete the first argument, which is the script
        del argv[0]
    # Logging
    if (enableLogging == "true"):
        # Setup logging
        logger, logMessage = setLogging(logFile)
        # Log start of process
        logger.info("Process started.")
    # Setup the use of a proxy for requests
    if (enableProxy == "true"):
        # Setup the proxy
        proxy = urllib2.ProxyHandler({requestProtocol : proxyURL})
        openURL = urllib2.build_opener(proxy)
        # Install the proxy
        urllib2.install_opener(openURL)
    mainFunction(*argv)
