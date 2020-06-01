#!/usr/bin/env python3

import requests as req
import threading
import time
import concurrent.futures
import datetime
import math

#from datetime import datetime

#f= open("guru99.txt","w+")
#f.write("This is line %d\r\n" % (i+1))
#f.close() 

def notifyStackdriver(responseTime):
    #url = "http://35.238.191.128:8081/" + str(round(responseTime, 0))
    url = "http://35.238.191.128:8081/" + str(math.ceil(responseTime))
    print(url)
    #resp = req.get("http://35.238.191.128:8081/333")
    resp = req.get(url)
    print(resp.text)

def millis_interval(start, end):
    """start and end are datetime instances"""
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return millis

def make_request(id):  
    while True:
        start = datetime.datetime.now()
        resp = req.get("http://35.224.99.170:2020//collector/datafromresource/1")
        end = datetime.datetime.now()
        diff = millis_interval(start, end)
        notifyStackdriver(diff)
	
        #update_url = new char[]("http://", SERVER_ADDRESS, ":2020/collector/data/1")
        url = "http://35.224.99.170:2020/collector/data/1"
        payload = {'username':'Olivia','password':'123','username1':'Olivia1','password1':'1231','username2':'Olivia2','password2':'1232','username4':'Olivia','password4':'123'}
#{"data": {"public_bus": [{"location": {"lat": -10.00032,"lon": -23.559615},"speed": 54,"uuid": 1,"bus_line": "875c-10-1","timestamp": "2017-06-14T17:52:25.428Z"}]}} #{'username':'Olivia','password':'123'}
        headers = {'content-type': 'application/json'}

        #response = requests.post(url, data=json.dumps(payload), headers=headers)
        #data = ""\"data\": {""
        resp2 = req.post(url, data=payload)#json.dumps(payload), headers=headers)

        print(id)
        print(resp.text)
        print(diff)
        f = open("responseTime_noPAL_withHPA00.data","a+")
        #f.write("This is line %d\r\n" % (diff))
        fileLine = "[" + str(end) + "] " + str(diff) + "\n"
        f.write(fileLine)
        f.close() 
    
if __name__ == "__main__": 
    main_start = datetime.datetime.now()
    make_request(1)
    #with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
     #   executor.map(make_request, 1)
    main_end = datetime.datetime.now()
    main_diff = millis_interval(main_start, main_end)
    print("total time ========================== ")
    print(main_diff)



