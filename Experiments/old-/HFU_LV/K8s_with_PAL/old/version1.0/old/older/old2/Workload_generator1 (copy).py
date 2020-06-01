#!/usr/bin/env python3

import requests as req
import threading
import time
import concurrent.futures
import datetime

NUM_THREADS_ARRAY = [10, 20, 50, 100, 150, 200]

def millis_interval(start, end):
    """start and end are datetime instances"""
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return millis

def make_request(id):
    start = datetime.datetime.now()  #milli_sec = int(round(time.time() * 1000))  #
    
    

    #resp = req.get("http://35.223.180.209:2020//collector/resources/1/data")
    resp = req.get("http://35.223.180.209:2020//collector/datafromresource/1")
    #resp = req.get("http://google.com")

    #flag = 0
    end = datetime.datetime.now()
    diff = millis_interval(start, end)

    """print("id: ", id)
    print("resp.text: ", resp.text)
    print("diff: ", diff)"""

    return diff



if __name__ == "__main__":
    total_time_start = datetime.datetime.now()

    sleep_time = 1
    diff_time1 = 0

    for round in NUM_THREADS_ARRAY:
        NUM_THREADS = round
        for i in range(1):
            print("sleep_time222: ", sleep_time)
            time.sleep(sleep_time)
            print(round)
            print(i) 
            threads_creating_time_start = datetime.datetime.now()
            with concurrent.futures.ThreadPoolExecutor(max_workers=round) as executor:
                start_time1 = datetime.datetime.now()
                results = executor.map(make_request, range(round))
                end_time1 = datetime.datetime.now()
                diff_time1 = millis_interval(start_time1, end_time1)
                print("total time123 ========================== ")
                print(diff_time1)
                sleep_time = (3000 - diff_time1)/1000
                print("total time456 ========================== ")
                print(sleep_time)

            real_results = list(results)
            print('main: results: {}'.format(real_results))




            threads_creating_time_end = datetime.datetime.now()
            threads_creating_time = millis_interval(threads_creating_time_start, threads_creating_time_end)
            #sleep_time = abs(1 - threads_creating_time)
            print("threads_creating_time ========================== ")
            print(threads_creating_time)

    total_time_end = datetime.datetime.now()
    main_diff = millis_interval(total_time_start, total_time_end)
    print("total time ========================== ")
    print(main_diff)

    """
    #f = open("totalResponseTime_noPAL_withHPA.data","a+")
    f = open("HFU_LV_WITHPAL_RESULTS/total_response_time_withPAL_withHPA.data","a+")
    #f.write("This is line %d\r\n" % (diff))
    #fileLine = "[" + str(end) + "] " + str(diff) + "\n"
    total_response_time = str(main_diff) + "\n"
    f.write(total_response_time)
    f.close() """



