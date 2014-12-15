'''
---------------------------------
URL Checking script
---------------------------------
This script will:

Check for valid URLs from a specified web site repo.

Date : December 10, 2014 

Author:        Avi - acueva@esri.com
Contributors:  
               
These scripts provided as samples and are not supported through Esri Technical Support.
Please direct questions to either the Python user forum : https://geonet.esri.com/community/developers/gis-developers/python

'''

import os
import re
import urllib2

#Set this path to web site repo you want to crawl.
PATH = "C:\\Users\\avel5840\\Documents\\GitHub\\arcgis-solutions-website-master\\source\\"

#Walks through directory structure looking for .erb files.
result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(PATH) for f in filenames if os.path.splitext(f)[1] == '.erb']

#Searches each file for referrences to http and https. If found then the URL is tested.
#Only returns output if there is a failure with the URL.  Returns the HTTP error code.
for item in result:
    searchfile = open(item,"r")
    for line in searchfile:
        if "href=\"http" in line:
            #Parse all items betwen quotes " "
            lineparse = re.findall('"([^"]*)"', line)
            if ("http" or "https") in lineparse[0]:
                #print lineparse[0]
                try:
                    urllib2.urlopen(lineparse[0])
                except urllib2.HTTPError, e:
                    print lineparse[0]
                    print(e.code)
                except urllib2.URLError, e:
                    print lineparse[0]
                    print(e.args)                
        searchfile.close

    
