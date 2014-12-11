'''
---------------------------------
URL Checking script
---------------------------------
This script will:

Check for valid URLs from a specified web site.

Date : December 10, 2014 

Author:        Avi - acueva@esri.com
Contributors:  
               
These scripts provided as samples and are not supported through Esri Technical Support.
Please direct questions to either the Python user forum : http://forums.arcgis.com/forums/117-Python
or the ArcGIS Server General : http://forums.arcgis.com/forums/8-ArcGIS-Server-General

'''

import os
import re

PATH = "C:\\Users\\avel5840\\Documents\\GitHub\\arcgis-solutions-website-master\\source\\military\\domestic-operations"

result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(PATH) for f in filenames if os.path.splitext(f)[1] == '.erb']

for item in result:
    searchfile = open(item,"r")
    for line in searchfile:
        #test = re.findall('"([^"]*)"', line)
        if "href=\"http://" in line:
            #Parse all items betwen quotes " "
            lineparse = re.findall('"([^"]*)"', line)
            print lineparse
                
            if "href=\"https://" in line:
                print line
        searchfile.close

    
#import urllib2
#
#try:
#    urllib2.urlopen('https://www.google.com/logos/doodles/2014/annie-jump-cannons-151st-birthday-5677811415121920rthrtp.jpg')
#except urllib2.HTTPError, e:
#    print(e.code)
#except urllib2.URLError, e:
#    print(e.args)