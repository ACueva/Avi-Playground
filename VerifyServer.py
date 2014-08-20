#!/usr/bin/env python
import os
import urllib2, json
from urlparse import urlparse

def ParseURL(agsURL):
    ags = []
    print agsURL
    ags = urlparse(agsURL)
    return ags

def GetFolders(agsURL):
    f = urllib2.urlopen(agsURL)
    j = json.loads(f.read())
    for item in j["folders"]:
        print item
               
def MapServiceQuery(agsURL):
    f = urllib2.urlopen(agsURL)
    #print f.read()
    j = json.loads(f.read())
    for item in j["layers"]:
        print item["name"]