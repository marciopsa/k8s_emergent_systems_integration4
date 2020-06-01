#!/usr/bin/env python3

import requests as req
import threading
import time
import concurrent.futures
import datetime
import math
import threading

NUM_THREADS_ARRAY = [1,2,4,8,16,32,64]#, 20, 50, 100, 150, 200]
MAX_VALUE = 17#68#200
MAX_EXPONENTIAL_VALUE = 16#64
y = 1

flag = 1

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

def checking_response_time_and_updating_dc():  
    while flag == 1:
        #time.sleep(5)
        try:
            start = datetime.datetime.now()
            resp = req.get("http://35.224.99.170:2020//collector/datafromresource/1")
            #resp = req.get("http://35.223.180.209:2020//collector/datafromresource/1")
            end = datetime.datetime.now()
            diff = millis_interval(start, end)
            notifyStackdriver(diff)
	
            try:
                url = "http://35.224.99.170:2020/collector/data/1"
                #url = "http://35.223.180.209:2020/collector/data/1"
                payload = {'username':'Olivia','password':'123','username1':'Olivia1','password1':'1231','username2':'Olivia2','password2':'1232','username4':'Olivia','password4':'123'}

                headers = {'content-type': 'application/json'}
                resp2 = req.post(url, data=payload)#json.dumps(payload), headers=headers)

                print(id)
                print(resp.text)
                print(diff)
                f = open("HFU_LV_WITHPAL_RESULTS/responseTime_withPAL_withHPA00.data","a+")
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
    #resp = req.get("http://35.223.180.209:2020//collector/datafromresource/1")
    resp = req.get("http://35.224.99.170:2020//collector/datafromresource/1")
    #resp = req.get("http://google.com")

    #flag = 0
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
        t = threading.Thread(target=checking_response_time_and_updating_dc)
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

    



    """for round in NUM_THREADS_ARRAY:
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
    print(main_diff)"""

    """
    #f = open("totalResponseTime_noPAL_withHPA.data","a+")
    f = open("HFU_LV_WITHPAL_RESULTS/total_response_time_withPAL_withHPA.data","a+")
    #f.write("This is line %d\r\n" % (diff))
    #fileLine = "[" + str(end) + "] " + str(diff) + "\n"
    total_response_time = str(main_diff) + "\n"
    f.write(total_response_time)
    f.close() """



