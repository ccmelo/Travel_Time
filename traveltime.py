
import numpy as np
import pandas
import os 
import requests 
#import json


#mode=driving 


 
def get_file_location(): 
    a=raw_input("Where is your csv file located? (I need the full file path please!")
    return a

def get_mode(): 
    a=raw_input("What mode of travel are you calculating travel times for? \
        \n enter D for driving, W for walking, or T for public transit") 
    return a 

def makerequests(property):
     origin=str(property['Latitude'])+","+str(property['Longitude'])
     destination="42.3587543,-71.060423"
     p={'key':'AIzaSyBaFlG4WjXyTu1_zy04IaIgbB-01OXPz1g', 'origins': origin, 'destinations': destination}
     r= requests.post('https://maps.googleapis.com/maps/api/distancematrix/json', params=p)
     return r.json()

def getduration(traveltime):
     return traveltime['rows'][0]['elements'][0]['duration']['value']

     
def getdistance(traveltime):
     return traveltime['rows'][0]['elements'][0]['distance']['value']



file_location=get_file_location()
filename=file_location.split('\\')[-1]
file_location='\\'.join(file_location.split('\\')[0:-1])



os.chdir(file_location)
data=pandas.read_csv(filename)
data['duration']=" "
data['distance']=" "
mode=get_mode

#for x in range(0,len(data.index)):
    #ttjson=makerequests(data.iloc[x]) 
    #data.ix[x,'duration']=getduration(ttjson)
   # data.ix[x,'distance']=getdistance(ttjson)


data.to_csv('sampleoutput.csv')