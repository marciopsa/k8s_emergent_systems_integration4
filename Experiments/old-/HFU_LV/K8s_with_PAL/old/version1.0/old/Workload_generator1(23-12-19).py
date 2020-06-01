#!/usr/bin/env python3

import requests as req
import threading
import time
import concurrent.futures
import datetime
import math
import threading
import statistics

MAX_VALUE = 100  		# max rate in the experiment (in requests per second)
MAX_EXPONENTIAL_VALUE = 64   	# max value of rate using an exponential function (2^y)
y = 1  				# the exponent in exponencial function (2^y)
flag = 1  			# this flag controls when updating_data_collector() function should stop.
UPDATE_TIME = 2 		# time interval for updating the database  (in seconds)



# This method sends response time values to Stackdriver Monitoring System. 
def notifyStackdriver(responseTime):
    try:
        url = "http://35.238.191.128:8081/" + str(math.ceil(responseTime))
        resp = req.get(url)
    except req.RequestException as e:
        if e.response is not None:
            print(e.response)
        else:
            print('no conection to metrics server (no requests)...')




# This method is responsible for updating the Data Collector database.
def updating_data_collector():  
    while flag == 1: 

        time.sleep(UPDATE_TIME)

        try:
            url = "http://35.224.99.170:2020/collector/data/1"
            #url = "http://35.223.180.209:2020/collector/data/1"
            payload = {'username':'Olivia','password':'123','username1':'Olivia1','password1':'1231','username2':'Olivia2','password2':'1232','username4':'Olivia','password4':'123'}

            headers = {'content-type': 'application/json'}
            response = req.post(url, data=payload)


            print("updating_data_response: ", response.text)
           
        
        
        except req.RequestException as e:
            if e.response is not None:
                print(e.response)
            else:
                print('no conection to DC server (no updates)...')


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
    start = datetime.datetime.now()  

    resp = req.get("http://35.224.99.170:2020//collector/datafromresource/1")

    end = datetime.datetime.now()
    diff = millis_interval(start, end)

    return diff



if __name__ == "__main__":
    total_time_start = datetime.datetime.now()
    
    response_time_set = []
 
    flag = 1
 
    threads = []
    for i in range(1):
        t = threading.Thread(target=updating_data_collector)
        threads.append(t)
        t.start()

    sleep_time = 1
    diff_time1 = 0

    i = 1
    while i < MAX_VALUE:
        print("sleep_time222: ", sleep_time)
        time.sleep(sleep_time)
        #print(round)
        print("value of i:",i) 
        threads_creating_time_start = datetime.datetime.now()
        with concurrent.futures.ThreadPoolExecutor(max_workers=i) as executor:
            start_time1 = datetime.datetime.now()
            results = executor.map(make_request, range(math.ceil(i)))
            end_time1 = datetime.datetime.now()
            diff_time1 = millis_interval(start_time1, end_time1)
            sleep_time = (3000 - diff_time1)/1000

        if (i < MAX_EXPONENTIAL_VALUE):
            temp = math.pow(2,y)
            i = math.ceil(temp)
            y = y + 1
        else: 
            i = i + 1
     
        real_results = list(results)
        response_time_set.append(real_results)

        average_response_time_value = statistics.mean(real_results) 
       
        thread1 = threading.Thread(target = notifyStackdriver, args = (average_response_time_value,))
        thread1.start()


        threads_creating_time_end = datetime.datetime.now()
        threads_creating_time = millis_interval(threads_creating_time_start, threads_creating_time_end)
        

    total_time_end = datetime.datetime.now()
    main_diff = millis_interval(total_time_start, total_time_end)
    flag = 0


    f = open("HFU_LV_NOPAL_RESULTS/total_response_time_noPAL_noHPA.data","a+")


    for i in range(len(response_time_set)):
        fileLine = "[" + str(response_time_set[i]) + "] " + "\n"
        f.write(fileLine)

    total_response_time = str(main_diff) + "\n"
    f.write(total_response_time)
    f.close()


