import numpy as np
import pandas
import os 
import requests 
#import json

os.chdir('C:/Users/cmelo/Documents/Travel Time')
filename= 'sampledata.csv'
data=pandas.read_csv(filename)
#mode=driving 


data['duration']=" "
data['distance']=" "
 

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

     
def getdistance(traveltime):
     return traveltime['rows'][0]['elements'][0]['distance']['value']

for x in range(0,len(data.index)):
    print x 
    ttjson=makerequests(data.iloc[x]) 
    data.ix[x,'duration']=getduration(ttjson)
    data.ix[x,'distance']=getdistance(ttjson)

#data.apply(gettraveltime, axis=1)
data.to_csv('sampleoutput.csv')