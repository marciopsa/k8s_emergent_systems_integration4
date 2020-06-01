#!/usr/bin/env python3

import requests as req
import threading
import time
import concurrent.futures
import datetime
import math
import threading
import statistics

MAX_VALUE = 100#200#17#68#
MAX_EXPONENTIAL_VALUE = 64#16#
y = 1  # 
flag = 1
UPDATE_TIME = 2 # (in seconds)

# This method sends response time values to Stackdriver Monitoring System. 
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


# This method is responsible for updating the Data Collector database.
def updating_data_collector():  
    while flag == 1: 

        time.sleep(UPDATE_TIME)

        try:
            url = "http://35.224.99.170:2020/collector/data/1"
            #url = "http://35.223.180.209:2020/collector/data/1"
            payload = {'username':'Olivia','password':'123','username1':'Olivia1','password1':'1231','username2':'Olivia2','password2':'1232','username4':'Olivia','password4':'123'}

            headers = {'content-type': 'application/json'}
            resp2 = req.post(url, data=payload)#json.dumps(payload), headers=headers)


            print("resp2: ", resp2.text)
           
        
        
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
    
    #resp = req.get("http://35.223.180.209:2020//collector/resources/1/data")
    #resp = req.get("http://35.223.180.209:2020//collector/datafromresource/1")
    resp = req.get("http://35.224.99.170:2020//collector/datafromresource/1")

    end = datetime.datetime.now()
    diff = millis_interval(start, end)

    #print("id: ", id)
    #print("resp.text: ", resp.text)
    #print("diff: ", diff)

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
            print("total time123 ========================== ")
            print(diff_time1)
            sleep_time = (3000 - diff_time1)/1000
            print("total time456 ========================== ")
            print(sleep_time)


        if (i < MAX_EXPONENTIAL_VALUE):
            temp = math.pow(2,y)
            i = math.ceil(temp)
            y = y + 1
        else: 
            i = i + 1
     
        real_results = list(results)
        print('main: results: {}'.format(real_results))
        response_time_set.append(real_results)

        average_response_time_value = statistics.mean(real_results) 
        print('Average_response_time_value: {}'.format(average_response_time_value))
        """threads1 = []
        for i in range(1):
            t = threading.Thread(target=notifyStackdriver, args = (average_response_time_value))
            threads1.append(t)
            t.start()"""
        thread1 = threading.Thread(target = notifyStackdriver, args = (average_response_time_value,))
        thread1.start()


        threads_creating_time_end = datetime.datetime.now()
        threads_creating_time = millis_interval(threads_creating_time_start, threads_creating_time_end)
        #sleep_time = abs(1 - threads_creating_time)
        print("threads_creating_time ========================== ")
        print(threads_creating_time)

    total_time_end = datetime.datetime.now()
    main_diff = millis_interval(total_time_start, total_time_end)
    flag = 0
    print("total time ========================== ")
    print(main_diff)

    #f = open("totalResponseTime_noPAL_withHPA.data","a+")
    f = open("HFU_LV_WITHPAL_RESULTS/total_response_time_withPAL_withHPA.data","a+")
    #f.write("This is line %d\r\n" % (diff))
    #fileLine = "[" + str(end) + "] " + str(diff) + "\n"

    for i in range(len(response_time_set)):
        #f.write("This is line \r\n" %(response_time_set[i]))
        fileLine = "[" + str(response_time_set[i]) + "] " + "\n"
        f.write(fileLine)
    total_response_time = str(main_diff) + "\n"
    f.write(total_response_time)
    f.close()


