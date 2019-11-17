#!/usr/bin/env python3

import requests as req
import threading
import time
import concurrent.futures

NUM_THREADS_ARRAY = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

def make_request(id):
    resp = req.get("http://35.239.83.45:2020//collector/datafromresource/1")	
    print(id)
    print(resp.text)


if __name__ == "__main__": 
    for round in NUM_THREADS_ARRAY:
        NUM_THREADS = round
        for i in range(100):
            time.sleep(1)
            print(round)
            print(i) 
            with concurrent.futures.ThreadPoolExecutor(max_workers=round) as executor:
                executor.map(make_request, range(round))




