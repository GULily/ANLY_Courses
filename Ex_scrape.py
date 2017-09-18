# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:13:55 2016

@author: Yi
"""

import requests
def main():
    AirNow()
def AirNow():
    # The Latitude - Lat - and Longitude - Long will be used to read in data from Air Now for AQI PM2.5 and Ozone
    Lat = []
    Long = []
    # Read Lat and Long data from file into list
    LatLong = open("LatLong.txt", "r")
    #The LatLong.txt must have this format: 34, -56.7
    for line in LatLong:
        if "\n" in line:
            #Remove the newline from each line
            line=(line.split(sep="\n"))[0]
        #Grab the Latitude from the line
        Lat.append(float((line.split(sep=","))[0]))
        #print(Lat)
        Long.append(float((line.split(sep=","))[1]))
        #print(Long.pop())
    LatLong.close()
    #print(Long)
    ScrapeAirNow(Lat, Long)
def ScrapeAirNow(Lat,Long):
    with open(“Ex_scrape_output.csv", "w") as OutFile:
    	date= '2016-09-13T00-0000'
    	# Setup parameters for API call
    	URLPost = {'API_KEY': 'C1D6711C-0566-44FC-9C39-33918F03FD85',
                    'latitude': 'placeholder',
                    'longitude':'placeholder',
                    'date': date,
                    'distance': '5',
                    'format': 'application/json'}
    	endpoint = "http://www.airnowapi.org/aq/observation/latLong/historical/"
    	# http://www.airnowapi.org/aq/observation/latLong/historical/?format=application/json&latitude=38.3651&longitude=-114.4141&date=2016-09-10T00-0000&distance=25&API_KEY=D9AA91E7-070D-4221-867C-XXXX
    	# For each Lat and Long, request data from the URL and write it to a file.
    	# Reverse Long so that elements can be "popped" off
    	Long.reverse()
    	for nextLat in Lat:
        	URLPost['latitude'] = nextLat
        	URLPost['longitude']=Long.pop()
        	#print(URLPost)
        	response=requests.get(endpoint, URLPost)
        	#txt = response.text
        	#print(txt)
        	# Get the json response and pull out fields to print
        	jsontxt = response.json()
        	for list in jsontxt:
            	#print("List is ", list)
            	AQIValue = str(list['AQI'])
            	State = list['StateCode']
            	City = list['ReportingArea']
            	Lati = str(list['Latitude'])
            	Longi = str(list['Longitude'])
            	print(State + "," + City + "," + Lati + "," + Longi + "," + AQIValue)
            	OutFile.write(State + "," + City + "," + Lati + "," + Longi + "," +
            	AQIValue + "\n")
    
main()


import urllib
from urllib.request import urlopen
def AirNow():
    ##http://www.airnowapi.org/aq/forecast/zipCode/?format=text/csv&zipCode=20007&date=2016-09-01&distance=25&API_KEY=D9AA91E7-070D-4221-867CEFF5E0D8C2C7
    #File=open(“Ex_scrape_AirNow.txt", "w", encoding="utf-8")
    #File.close()
    baseURL="http://www.airnowapi.org/aq/"
    (latitude,longitude) = (39,-77)
    date='2016-09-01'
    miles=25
    zipcode="20007"
    LatLngURL=baseURL + "forecast/latLong/?" + urllib.parse.urlencode({
    'format': "text/csv",
    'latitude': latitude,
    'longitude': longitude,
    'date':date,
    'distance':miles,
    'API_KEY':'C1D6711C-0566-44FC-9C39-33918F03FD85'
    })
    #print(LatLngURL)
    zipURL=baseURL + "forecast/zipCode/?" + urllib.parse.urlencode({
    'format': "text/csv",
    'zipCode':zipcode,
    'date':date,
    'distance':miles,
    'API_KEY':'C1D6711C-0566-44FC-9C39-33918F03FD85'
    })
    #print(zipURL)
    #File=open(“Ex_scrape_AirNow.txt", "w")
    for URL in [LatLngURL]:
    #for URL in [zipURL]:
    #for URL in [LatLngURL,zipURL]:
        response=urlopen(URL).read().decode('utf-8')
        print(response)
    #File.write(response)
    #File.close()
AirNow()