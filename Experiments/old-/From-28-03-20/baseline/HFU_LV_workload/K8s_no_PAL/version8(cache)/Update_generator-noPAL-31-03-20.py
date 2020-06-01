#!/usr/bin/env python3.6

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
UPDATE_TIME = 0.05		# time interval for updating the database  (in seconds)
NOTIFY_STACKDRIVER_TIME = 10


NUM_THREADS_ARRAY = [4]#,71,72,73,74,75,76,77,78,79,80]#, 20, 50, 100, 150, 200]#

HFU_LV_REQUEST_URL = "http://35.224.101.35:2020/collector/datafromresource/1"
LFU_HV_REQUEST_URL = "http://35.224.101.35:2020//collector/resources/1/data"
STACKDRIVER_URL = "http://35.239.239.83:8081/"
UPDATING_URL = "http://35.224.101.35:2020/collector/data/1"


TOTAL_RESPONSE_DATA_LIST = []

response_time_set = []
average_response_time_set = []
rps_for_each_burst_of_request = []
number_of_requests_with_response_time_less_than_one_second = 0
average_rps_for_each_burst_of_request = []
number_of_none_results_list = []

values_sent_to_stackdriver_list = []
values_sent_to_stackdriver_index = 0

current_average_response_time_value = 0

NUMBER_OF_SEQ_ROUNDS = 10

future_list = []
real_results = []


# receives two timestamps and calculate the time interval between them
def millis_interval(start, end):
    """start and end are datetime instances"""
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return millis

# This method is responsible for updating the Data Collector database.
def updating_data_collector():  
    while flag == 1: 

        time.sleep(UPDATE_TIME)

        try:
            url = UPDATING_URL #"http://35.202.100.82:2020/collector/data/1"
            #url = "http://35.223.180.209:2020/collector/data/1"
            payload = {'username':'Olivia','password':'123','username1':'Olivia1','password1':'1231','username2':'Olivia2','password2':'1232','username4':'Olivia','password4':'123'}

            headers = {'content-type': 'application/json'}
            response = req.post(url, data=payload)#json.dumps(payload), headers=headers)


            print("updating_data_response: ", response.content)
           
        
        
        except req.RequestException as e:
            if e.response is not None:
                print(e.response)
            else:
                print('no conection to DC server (no updates)...')








if __name__ == "__main__": 
    total_time_start = datetime.datetime.now()

    flag = 1
 
    threads = []
    for i in range(4):
        t = threading.Thread(target=updating_data_collector)
        threads.append(t)
        t.start()


    




   
