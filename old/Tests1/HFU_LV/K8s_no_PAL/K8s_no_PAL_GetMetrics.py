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

        print(id)
        print(resp.text)
        print(diff)
        f = open("responseTime1.data","a+")
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



