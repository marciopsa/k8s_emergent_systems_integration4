#!/usr/bin/env python3

import requests as req
import threading
import time
import concurrent.futures
import datetime
import math
import threading
import statistics


class ResponseData:
    url = ""
    response_content = ""
    response_status_code = ""
    response_time = 0


    
    

MAX_VALUE = 10  		# max rate in the experiment (in requests per second)
MAX_EXPONENTIAL_VALUE = 64   	# max value of rate using an exponential function (2^y)
y = 1  				# the exponent in exponencial function (2^y)
flag = 1  			# this flag controls when updating_data_collector() function should stop.
UPDATE_TIME = 2 		# time interval for updating the database  (in seconds)


URL = "http://35.225.247.127:2020/collector/datafromresource/1"

TOTAL_RESPONSE_DATA_LIST = []


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
    #resp = req.get("http://example.com")
    #print("resp.text1: ", resp.status_code)
    #print("resp.text1: ", resp.content)
    end = datetime.datetime.now()
    diff = millis_interval(start, end)

    resp_data = ResponseData()
    resp_data.url = URL
    resp_data.response_content = resp.content
    resp_data.response_status_code = resp.status_code
    resp_data.response_time = diff
    

    return resp_data



if __name__ == "__main__":
    total_time_start = datetime.datetime.now()   # It stores the timestamp of beginning of the script execution.
 
    i = 1
    while i <= MAX_VALUE:  #True: #i <= MAX_VALUE:     # MAX_VALUE controls the max rate (in requests per second) in the experiment 
        oneRequestTime_start = datetime.datetime.now()
        resp_data = make_request()
        oneRequestTime_end = datetime.datetime.now()
        diff = millis_interval(oneRequestTime_start, oneRequestTime_end)
        print("request time (ms): ", diff)
        print("resp_data.response_time: ", resp_data.response_time)
        TOTAL_RESPONSE_DATA_LIST.append(resp_data)
        i = i + 1
    total_time_end = datetime.datetime.now()   # It stores the timestamp of end of the script execution.
    total_diff = millis_interval(total_time_start, total_time_end)

    # After the end of the execution, the data will be stored in a file.
    f = open("HFU_LV_WITHPAL_RESULTS/total_response_time_noPAL_noHPA.data","a+")

    for i in range(len(TOTAL_RESPONSE_DATA_LIST)):
        print("TOTAL_RESPONSE_DATA_LIST: ", TOTAL_RESPONSE_DATA_LIST[i].response_time)
        fileLine = "[" + str(TOTAL_RESPONSE_DATA_LIST[i].response_time) + "] " + "\n" # It stores, at each line, the response times obtained from each rate selected
        f.write(fileLine)

    
    total_execution_time = "TOTAL EXECUTION TIME: " + str(total_diff) + "\n"  
    iterations = "ITERATIONS: " + str(MAX_VALUE) + "\n"   
    average_response_time = total_diff/MAX_VALUE
    avg_resp_time = "AVERAGE RESPONSE TIME: " + str(average_response_time) + "\n"
    f.write(iterations)
    f.write(avg_resp_time)
    f.write(total_execution_time)    # The total execution time is also stored at the final of the same file.
    f.close()

