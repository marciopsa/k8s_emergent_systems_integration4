#!/usr/bin/env python3

import requests as req
import threading
import time
import concurrent.futures
import datetime
import math
import threading
import statistics

MAX_VALUE = 80  		# max rate in the experiment (in requests per second)
MAX_EXPONENTIAL_VALUE = 64   	# max value of rate using an exponential function (2^y)
y = 1  				# the exponent in exponencial function (2^y)
flag = 1  			# this flag controls when updating_data_collector() function should stop.
UPDATE_TIME = 2 		# time interval for updating the database  (in seconds)






# receives two timestamps and calculate the time interval between them
def millis_interval(start, end):
    """start and end are datetime instances"""
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return millis

# This method is responsible for making requests to Interscity's Data Collector
#def make_request(id):
def make_request():
    start = datetime.datetime.now()  

    #resp = req.get("http://35.225.247.127:2020/collector/datafromresource/1")
    resp = req.get("http://google.com")
    #print("resp.text1: ", resp.status_code)
    print("resp.text1: ", resp.content)
    end = datetime.datetime.now()
    diff = millis_interval(start, end)

    return diff



if __name__ == "__main__":
    total_time_start = datetime.datetime.now()   # It stores the timestamp of beginning of the script execution.
 
    while True: #i <= MAX_VALUE:     # MAX_VALUE controls the max rate (in requests per second) in the experiment 
        oneRequestTime_start = datetime.datetime.now()
        make_request()
        oneRequestTime_end = datetime.datetime.now()
        diff = millis_interval(oneRequestTime_start, oneRequestTime_end)
        print("request time (ms): ", diff)
        



