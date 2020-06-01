#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
from time import sleep
 
def return_after_2_secs(message):
    sleep(2)
    return message
 
pool = ThreadPoolExecutor(3)
 
future = pool.submit(return_after_2_secs, ("hello1"))
print(future.done())
sleep(2)
print(future.done())
sleep(2)
print(future.done())
print(future.result())



