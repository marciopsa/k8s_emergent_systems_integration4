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
UPDATE_TIME = 10 		# time interval for updating the database  (in seconds)


NUM_THREADS_ARRAY = [1,2,4,8,16,32,64,65,66,67,68,69,70]#,71,72,73,74,75,76,77,78,79,80]#, 20, 50, 100, 150, 200]#

REQUEST_URL = "http://35.202.100.82:2020/collector/datafromresource/1"
STACKDRIVER_URL = "http://35.238.193.242:8081/"
UPDATING_URL = "http://35.202.100.82:2020/collector/data/1"

TOTAL_RESPONSE_DATA_LIST = []

response_time_set = []
average_response_time_set = []

current_average_response_time_value = 0

NUMBER_OF_SEQ_ROUNDS = 30

future_list = []
real_results = []

# This method sends response time values to Stackdriver Monitoring System. 
def notifyStackdriver(responseTime):
    try:
        url = STACKDRIVER_URL + str(math.ceil(responseTime))
        print(url)
        resp = req.get(url)
        print(resp.text)
    except req.RequestException as e:
        if e.response is not None:
            print(e.response)
        else:
            print('no conection to metrics server (no requests)...')

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

# This method is responsible for making requests to Interscity's Data Collector
def make_request(id):
#def make_request(): 
    try:
        start = datetime.datetime.now()  
        #resp = req.get("http://35.202.100.82:2020/collector/datafromresource/1")
        resp = req.get(REQUEST_URL)
        end = datetime.datetime.now()
        diff = millis_interval(start, end)
        print("single response time: ", diff)

        resp_data = ResponseData()
        resp_data.url = REQUEST_URL
        resp_data.response_content = resp.content
        resp_data.response_status_code = resp.status_code
        resp_data.response_time = diff
        #return resp_data
        return diff

    except req.RequestException as e:
        if e.response is not None:
            print(e.response)
        else:
            print('no conection to DC server (no requests)...')


if __name__ == "__main__": 
    total_time_start = datetime.datetime.now()

    flag = 1
 
    threads = []
    for i in range(1):
        t = threading.Thread(target=updating_data_collector)
        threads.append(t)
        t.start()

    for round in NUM_THREADS_ARRAY:
        for i in range(NUMBER_OF_SEQ_ROUNDS):
            real_results = []
            future_list = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=round) as executor:
                main_start = datetime.datetime.now()
                #results = executor.map(make_request, range(round))
                print("RESULTS =12233========================= ")#, results[0])
                for arg in range(round):
                    future = executor.submit(make_request, arg)
                    future_list.append(future)

                
                for future in future_list:
                    try: 
                        print("future.result(): ", future.result())
                        single_result = future.result()
                        if single_result is not None:
                            real_results.append(single_result)
                    except Exception as e:
                        print("Exception in futures.ThreadPoolExecutor: ", e)

                
                response_time_set.append(real_results)

                #real_results = list(results)
                #response_time_set.append(real_results)
                main_end = datetime.datetime.now()
                main_diff = millis_interval(main_start, main_end)
                print("partial time ========================== ", main_diff)

                

            #if real_results is not None:
            print("REAL RESULTS SIZE: ", len(real_results))
            real_results_size = len(real_results)
            if real_results_size > 0:
                for value in real_results:
                    print("value1111: ", value)
                current_average_response_time_value = statistics.mean(real_results)

            else:
                current_average_response_time_value = 1
            #current_average_response_time_value = 111
            #current_average_response_time_value = statistics.mean(real_results)
            average_response_time_set.append(current_average_response_time_value)
            print("current_average_response_time_value ====  ====  ====  ====  ========== ", current_average_response_time_value)
            print("==== NUMBER OF THREADS ==================================: ", round)
            print("==== ITERATION ==========================================: ", i)
        thread1 = threading.Thread(target = notifyStackdriver, args = (current_average_response_time_value,))
        thread1.start()
    
    flag = 0

   

    total_time_end = datetime.datetime.now()   # It stores the timestamp of end of the script execution.
    total_diff = millis_interval(total_time_start, total_time_end)

    print("total time ========================== ")
    print(total_diff)

    

    # After the end of the execution, the data will be stored in a file.
    f = open("HFU_LV_NOPAL_RESULTS/Response_time_noPAL_noHPA(0).data","a+")

    for i in range(len(response_time_set)):
        fileLine = "[" + str(response_time_set[i]) + "] " + "\n"
        f.write(fileLine)


    for i in range(len(average_response_time_set)):
        fileLine = "average response time [" + str(i) + "]" + str(average_response_time_set[i]) + "\n"
        f.write(fileLine)

    number_of_sequental_rounds = "NUMBER OF SEQ. ROUNDS: " + str(NUMBER_OF_SEQ_ROUNDS) + "\n"   
    num_of_threads = "NUMBER OF THREADS: " + str(NUM_THREADS_ARRAY) + "\n" 

    f.write(num_of_threads)
    f.write("WORKLOAD: HFU_LV; PAL CONFIG: default \n") #; NUMBER OF REPLICAS: 1 \n")

    total_execution_time = "TOTAL EXECUTION TIME (Concurrent Parallel Requests): " + str(total_diff) + "\n" 

    #total_execution_time = "TOTAL EXECUTION TIME: " + str(total_diff) + "\n"    
    f.write(total_execution_time + "\n\n")    # The total execution time is also stored at the final of the same file.
    f.close()




