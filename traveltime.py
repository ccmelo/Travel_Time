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

def gettraveltime(property):
     print property
     origin=str(property['Latitude'])+","+str(property['Longitude'])
     destination="42.3587543,-71.060423"
     print origin 
     print destination
     p={'key':'AIzaSyBaFlG4WjXyTu1_zy04IaIgbB-01OXPz1g', 'origins': origin, 'destinations': destination}
     r= requests.post('https://maps.googleapis.com/maps/api/distancematrix/json', params=p)
     print r.url
     a=r.json()
     print a
     duration= pandas.Series(a['rows'][0]['elements'][0]['duration']['value'], index=['duration'])
     property=pandas.concat([property,duration],axis=0)
     return property 
     
result=pandas.DataFrame()     
for x in (0,len(data.index)):
    print x 
    newrow=gettraveltime(data.iloc[x])
    if x==0:
        result.loc['0']=pandas.DataFrame(newrow)
    else:
        pandas.concat([result,newrow])
    print "FUNCTION RESULT"
    print newrow
    print result
#data.apply(gettraveltime, axis=1)
