#!/usr/bin/env python3

import timeit


code_to_test = """
def make_request():
    start = datetime.datetime.now()  
    resp = req.get("http://35.223.180.209:2020//collector/datafromresource/1")
    end = datetime.datetime.now()
    diff = millis_interval(start, end)
    print("diff: ", diff)
    
if __name__ == "__main__":

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(make_request, range(100))
"""

elapsed_time = timeit.timeit(code_to_test, number=100)
print(elapsed_time)
