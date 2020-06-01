#!/usr/bin/env python3

import requests as req
import threading
import time
import concurrent.futures
import datetime
import math

def make_request(id):  
    
    try:
        url = "http://35.223.180.209:2020/collector/data/1"
        payload = {'username':'Olivia','password':'123','username1':'Olivia1','password1':'1231','username2':'Olivia2','password2':'1232','username4':'Olivia','password4':'123'}

        headers = {'content-type': 'application/json'}
        resp2 = req.post(url, data=payload)
        print("updated")
    except req.RequestException as e:
        if e.response is not None:
            print(e.response)
        else:
            print('no conection to DC server (no updates)...')
        
    
if __name__ == "__main__": 
    print('rrrrrrrr')
    while True:
        time.sleep(5) 
        x = threading.Thread(target=make_request, args=(1,))
        x.start()
