import numpy as np
import pandas
import os 
import requests 
#import json

os.chdir('/Users/cmelo/Google Drive/Python')
filename= 'sampledata.csv'
data=pandas.read_csv(filename)
#mode=driving 

print data 
data['duration']=" "
print data 

def makerequests(property):
     print "in make requests"
     print property
     print "here"
     origin=str(property['Latitude'])+","+str(property['Longitude'])
     destination="42.3587543,-71.060423"
     print origin 
     print destination
     p={'key':'AIzaSyBaFlG4WjXyTu1_zy04IaIgbB-01OXPz1g', 'origins': origin, 'destinations': destination}
     r= requests.post('https://maps.googleapis.com/maps/api/distancematrix/json', params=p)
     print r.url
     return r.json()

def getduration(traveltime):
     return traveltime['rows'][0]['elements'][0]['duration']['value']

     

for x in range(0,len(data.index)):
    print x 
    ttjson=makerequests(data.iloc[x]) 
    print ttjson 
    print data.loc[x]
    print data['duration']
    data.ix[x,'duration']=getduration(ttjson)
    print data 
#data.apply(gettraveltime, axis=1)
