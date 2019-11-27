#!/usr/bin/env python3

import requests as req
import threading
import time
import concurrent.futures
import datetime

NUM_THREADS_ARRAY = [10, 20, 30, 40, 50, 100, 150, 200]#, 250]#, 300]#, 400, 500, 600, 700, 800, 900, 1000]

def millis_interval(start, end):
    """start and end are datetime instances"""
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return millis

def make_request(id):
    start = datetime.datetime.now()  #milli_sec = int(round(time.time() * 1000))  #
    #resp = req.get("http://35.239.83.45:2020//collector/datafromresource/1")
    resp = req.get("http://34.68.79.114:2020//collector/datafromresource/1")
    end = datetime.datetime.now()
    diff = millis_interval(start, end)
    #diff = int(delta.total_seconds() * 1000) # milliseconds
    #diff = (delta.days * 86400000) + (delta.seconds * 1000) + (delta.microseconds / 1000)	
    print(id)
    print(resp.text)
    print(diff)


if __name__ == "__main__": 
    main_start = datetime.datetime.now()
    for round in NUM_THREADS_ARRAY:
        NUM_THREADS = round
        for i in range(10):
            time.sleep(1)
            print(round)
            print(i) 
            with concurrent.futures.ThreadPoolExecutor(max_workers=round) as executor:
                executor.map(make_request, range(round))
    main_end = datetime.datetime.now()
    main_diff = millis_interval(main_start, main_end)
    print("total time ========================== ")
    print(main_diff)



