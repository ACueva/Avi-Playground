#!/usr/bin/env python
import unittest
import VerifyServer, listServices
import os
import getpass

#***********Start of User Configuration***********

#Enter ArcGIS Server URL in the following format:
# <Protocol>://<servername>/<Instance>
# Example http://sampleserver1.arcgisonline.com/ArcGIS

ArcGISURL = 'http://afmcloud.esri.com/ArcGIS'
AdminUser = "admin"
AdminPass = getpass.getpass(prompt="Please enter your ArcGIS Server password: ")


#***********End of User Configuration***********

ags = VerifyServer.ParseURL(ArcGISURL) 
print ags

if ags.scheme == 'http':
    port = 80
else:
    port = 443

services = listServices.getServiceList(ags.netloc, port, AdminUser, AdminPass)
print services

class TestAGSServices(unittest.TestCase):
    
    def setUp(self):
        #INPUT: SERVER URL
        #PARSE: hostname, ArcGIS Instance, SSL (Yes/No)    
        pass
                        
    def compare_services(self):
        #####---------------------------------------------------------------------------
        #####CMoore added here:
        #    
        #defaultCheckName = "ExpectedServiceList.txt"  
        #checkFileName = os.path.join(os.path.dirname(__file__), defaultCheckName)
        #
        #if not os.path.isfile(checkFileName) :
        #    raise Exception("Check file not found:" + checkFileName)        
        #
        #checkFile=open(checkFileName, "r")
        #lines = checkFile.readlines()
        #for line in lines :
        #    currentServiceToCheck = line.strip() #get rid of whitespace/newlines
        #    if not (currentServiceToCheck in serviceList) :
        #        print "Could not find required service: " + currentServiceToCheck            
        #
        ## write out for comparison::
        #defaultOutputName = "ServiceList.txt"   
        #outputFileName = os.path.join(os.path.dirname(__file__), defaultOutputName)  
        #outputFile=open(outputFileName, "w")
        #for serviceEntry in serviceList :
        #    outputFile.write(serviceEntry + "\n")
        #
        ####---------------------------------------------------------------------------
        pass
    
    def test_GetServices(self):
        pass    

    def test_RestEndpoint(self):
        #VerifyServer.GetFolders('http://sampleserver1.arcgisonline.com/ArcGIS/rest/services?f=pjson')
        pass
    
    #def test_Services(self):
    #    #VerifyServer.MapServiceQuery('http://sampleserver1.arcgisonline.com/ArcGIS/rest/services/WaterTemplate/LocalGovernmentInfrastructureBasemap/MapServer?f=pjson')
    #   #http://sampleserver1.arcgisonline.com/ArcGIS/rest/services/WaterTemplate/LocalGovernmentInfrastructureBasemap/MapServer?f=pjson
    #    pass
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
    