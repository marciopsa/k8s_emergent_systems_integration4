#!/usr/bin/python3.5
import asyncio
from aiohttp import ClientSession

async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)
            print("\n")




if __name__ == "__main__":
    #total_time_start = datetime.datetime.now()
    loop = asyncio.get_event_loop()


    for i in range(4):
        loop.run_until_complete(hello("http://35.223.180.209:2020//collector/resources/1/data"))
