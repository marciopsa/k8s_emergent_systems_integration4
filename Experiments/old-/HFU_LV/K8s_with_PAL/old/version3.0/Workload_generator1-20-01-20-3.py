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


MAX_VALUE = 80  		# max rate in the experiment (in requests per second)
MAX_EXPONENTIAL_VALUE = 64   	# max value of rate using an exponential function (2^y)
y = 1  				# the exponent in exponencial function (2^y)
flag = 1  			# this flag controls when updating_data_collector() function should stop.
UPDATE_TIME = 2 		# time interval for updating the database  (in seconds)


NUM_THREADS_ARRAY = [4]#, 20, 50, 100, 150, 200]#[10, 20, 30, 40, 50, 100, 150, 200]#, 250]#, 300]#, 400, 500, 600, 700, 800, 900, 1000]

URL = "http://34.68.110.63:2020/collector/datafromresource/1"

TOTAL_RESPONSE_DATA_LIST = []

response_time_set = []

NUMBER_OF_SEQ_ROUNDS = 1

# receives two timestamps and calculate the time interval between them
def millis_interval(start, end):
    """start and end are datetime instances"""
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return millis

# This method is responsible for making requests to Interscity's Data Collector
def make_request(id):
#def make_request():
    start = datetime.datetime.now()  
    resp = req.get("http://34.68.110.63:2020/collector/datafromresource/1")
    #resp = req.get("http://34.68.110.63:2020/collector/datafromresource/1")
    #resp = req.get("http://google.com")
    #print("resp.text1: ", resp.status_code)
    #print("resp.text1: ", resp.content)
    end = datetime.datetime.now()
    diff = millis_interval(start, end)
    print("single response time: ", diff)

    resp_data = ResponseData()
    resp_data.url = URL
    resp_data.response_content = resp.content
    resp_data.response_status_code = resp.status_code
    resp_data.response_time = diff
    

    #return resp_data
    return diff

def intermediate_func(thread_num):
    

    main_start = datetime.datetime.now()
    

    #time.sleep(1)
    print("thread_num: ", thread_num)
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_num) as executor:
        #executor.map(make_request, range(round))
        results = executor.map(make_request, range(round))

        real_results = list(results)
        response_time_set.append(real_results)
    main_end = datetime.datetime.now()
    main_diff = millis_interval(main_start, main_end)
    print("partial time ========================== ", main_diff)
    #print(main_diff)
    return statistics.mean(real_results)


if __name__ == "__main__": 
    total_time_start = datetime.datetime.now()
    average_response_time = 0
    for round in NUM_THREADS_ARRAY:
        NUM_THREADS = round
        for i in range(NUMBER_OF_SEQ_ROUNDS):
            average_response_time = intermediate_func(round)
    

    """main_end = datetime.datetime.now()
    main_diff = millis_interval(main_start, main_end)
    print("total time ========================== ")
    print(main_diff)"""

    total_time_end = datetime.datetime.now()   # It stores the timestamp of end of the script execution.
    total_diff = millis_interval(total_time_start, total_time_end)
    """main_end = datetime.datetime.now()
    main_diff = millis_interval(main_start, main_end)"""
    print("total time ========================== ")
    print(total_diff)

    

    # After the end of the execution, the data will be stored in a file.
    f = open("HFU_LV_WITHPAL_RESULTS/total_response_time_withPAL_noHPA(2replicas)(2).data","a+")

    for i in range(len(response_time_set)):
        fileLine = "[" + str(response_time_set[i]) + "] " + "\n"
        f.write(fileLine)

    """for i in range(len(TOTAL_RESPONSE_DATA_LIST)):
        print("TOTAL_RESPONSE_DATA_LIST: ", TOTAL_RESPONSE_DATA_LIST[i].response_time)
        fileLine = "[" + str(TOTAL_RESPONSE_DATA_LIST[i].response_time) + "] " + "\n" # It stores, at each line, the response times obtained from each rate selected
        f.write(fileLine)"""

    #average_response_time = statistics.mean(real_results)
    f.write("AVERAGE RESPONSE TIME: " + str(average_response_time) + "\n")
    number_of_sequental_rounds = "NUMBER OF SEQ. ROUNDS: " + str(NUMBER_OF_SEQ_ROUNDS) + "\n"   
    num_of_threads = "NUMBER OF THREADS: " + str(NUM_THREADS_ARRAY) + "\n" 

    f.write(num_of_threads)
    f.write("WORKLOAD: LV_HF; PAL CONFIG: cache; NUMBER OF REPLICAS: 2 \n")

    total_execution_time = "TOTAL EXECUTION TIME (Concurrent Parallel Requests): " + str(total_diff) + "\n" 

    #total_execution_time = "TOTAL EXECUTION TIME: " + str(total_diff) + "\n"    
    f.write(total_execution_time + "\n\n")    # The total execution time is also stored at the final of the same file.
    f.close()

        



