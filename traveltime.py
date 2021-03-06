
import numpy as np
import pandas
import os 
import requests 
#import json


#mode=driving 


 
def get_file_location(): 
    a=raw_input("Where is your csv file located? (I need the full file path please!)  ")
    return a

def get_mode(): 
    a=raw_input("What mode of travel are you calculating travel times for? \
        \n enter D for driving, W for walking, or T for public transit  ") 
    if a=='D':
        return 'driving'
    if a=='W':
        return 'walking'
    else: 
        return 'transit'

def makerequests(property, mode):
     origin=str(property['Origin_Lat'])+","+str(property['Origin_Long'])
     destination=str(property['Destination_Lat'])+","+str(property['Destination_Long'])
     p={'key':'AIzaSyBaFlG4WjXyTu1_zy04IaIgbB-01OXPz1g', 'origins': origin, 'destinations': destination, 'mode':mode}
     r= requests.post('https://maps.googleapis.com/maps/api/distancematrix/json', params=p)
     return r.json()

def getduration(traveltime):
     return traveltime['rows'][0]['elements'][0]['duration']['value']

     
def getdistance(traveltime):
     return traveltime['rows'][0]['elements'][0]['distance']['value']




file_location=get_file_location()
data=pandas.read_csv(file_location)
data['duration']=" "
data['distance']=" "
mode=get_mode()


for x in range(0,len(data.index)):
    ttjson=makerequests(data.iloc[x],mode) 
    data.ix[x,'duration']=getduration(ttjson)
    data.ix[x,'distance']=getdistance(ttjson)


data.to_csv('sampleoutput.csv')