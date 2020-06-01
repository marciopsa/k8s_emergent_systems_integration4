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
    try:
        url = "http://35.238.191.128:8081/" + str(math.ceil(responseTime))
        print(url)
        resp = req.get(url)
        print(resp.text)
    except req.RequestException as e:
        if e.response is not None:
            print(e.response)
        else:
            print('no conection to metrics server (no updates)...')

def millis_interval(start, end):
    """start and end are datetime instances"""
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return millis

def make_request(id):  
    while True:
        time.sleep(1)
        try:
            start = datetime.datetime.now()
            resp = req.get("http://35.224.99.170:2020//collector/datafromresource/1")
            end = datetime.datetime.now()
            diff = millis_interval(start, end)
            notifyStackdriver(diff)
	
            try:
                url = "http://35.224.99.170:2020/collector/data/1"
                payload = {'username':'Olivia','password':'123','username1':'Olivia1','password1':'1231','username2':'Olivia2','password2':'1232','username4':'Olivia','password4':'123'}

                headers = {'content-type': 'application/json'}
                resp2 = req.post(url, data=payload)#json.dumps(payload), headers=headers)

                print(id)
                print(resp.text)
                print(diff)
                f = open("HFU_LV_NOPAL_RESULTS/responseTime_noPAL_withHPA00.data","a+")
                #f.write("This is line %d\r\n" % (diff))
                fileLine = "[" + str(end) + "] " + str(diff) + "\n"
                f.write(fileLine)
                f.close() 
            except req.RequestException as e:
                if e.response is not None:
                    print(e.response)
                else:
                    print('no conection to DC server (no updates)...')



        except req.RequestException as e:
            if e.response is not None:
                print(e.response)
            else:
                print('no conection to DC server (no requests)...')
        
    
if __name__ == "__main__": 
    main_start = datetime.datetime.now()
    make_request(1)
    #with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
     #   executor.map(make_request, 1)
    main_end = datetime.datetime.now()
    main_diff = millis_interval(main_start, main_end)
    print("total time ========================== ")
    print(main_diff)



