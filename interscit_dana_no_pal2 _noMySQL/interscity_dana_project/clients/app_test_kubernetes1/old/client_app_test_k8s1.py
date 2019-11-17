#!/usr/bin/env python3

import requests as req
import threading
import time
import concurrent.futures

NUM_THREADS_ARRAY = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

def make_request(id, iteration):
    resp = req.get("http://35.239.83.45:2020//collector/datafromresource/1")	
    print(i)
    print(resp.text)


if __name__ == "__main__":
    
    for round in NUM_THREADS_ARRAY:
        NUM_THREADS = round
	for i in range(100):
            time.sleep(1)
            with concurrent.futures.ThreadPoolExecutor(max_workers=round) as executor:
            executor.map(make_request, range(round))



for round in NUM_THREADS_ARRAY:
    NUM_THREADS = round


for i in range(100):
    time.sleep(1)
    


=============================================================

    resp = req.get("http://35.239.83.45:2020//collector/datafromresource/1")	
    print(i)
    print(resp.text)




import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")













# Program to cancel the timer 
import threading 
  
def gfg(): 
    print("GeeksforGeeks\n") 
  
timer = threading.Timer(5.0, gfg) 
timer.start()



int App:main(AppParam params[]) {
		Thread t[] //= new Thread[NUM_THREADS]
		for (int round = 0; round < 10; round++) {
		   NUM_THREADS = NUM_THREADS_ARRAY[round]
		   t = new Thread[NUM_THREADS]
		   for (int i = 0; i < 100; i++) {
			timer.sleep(1000) 
			for (int counter = 0; counter < NUM_THREADS; counter++) { t[counter] = asynch::makeRequest("", counter, i) }
			for (int counter = 0; counter < NUM_THREADS; counter++) { t[counter].join() }
		   }
		   out.println("Modifying the workload...  next round: $(iu.intToString(round+1))")
		   timer.sleep(60000) 	
		}
		return 0
	}


void makeRequest(char resource[], int id, int i) {
		DateTime start = calendar.getTime()
		DateTime firstByte = new DateTime()
		HTTPResponse resp = http.get(new char[]("http://", server, ":2020//collector/datafromresource/1"), null)
		DateTime end = calendar.getTime()
		DateTime diff = dateUtil.diff(start, end)
		
		int response_time = dateUtil.toMilliseconds(diff)
		accumulated_response_time = accumulated_response_time + response_time
		request_counter++
		/*if (request_counter == 50) {
			notify_stackdriver()
		} */
		

		out.println("[$(iu.intToString(id))]: $(iu.intToString(dateUtil.toMilliseconds(diff)))")
		out.println("resp.content..: $(resp.content)")
		out.println("response_time..: $(iu.intToString(response_time))")
		out.println("accumulated_response_time..: $(iu.intToString(accumulated_response_time))")
		out.println("request_counter..: $(iu.intToString(request_counter))")		
	}
