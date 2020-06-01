#!/usr/bin/python3.5
import asyncio
import aiohttp
import tqdm


async def fetch(session, url):
    with aiohttp.Timeout(10, loop=session.loop):
        async with session.get(url) as response:
            return await response.text()


async def run(r):
    url = "http://35.223.180.209:2020//collector/resources/1/data"
    tasks = []
    # The default connection is only 20 - you want to stress...
    conn = aiohttp.TCPConnector(limit=1000)
    tasks, responses = [], []
    async with aiohttp.ClientSession(connector=conn) as session:
        tasks = [asyncio.ensure_future(fetch(session, url)) for _ in range(r)]
        #This will show you some progress bar on the responses 
        for f in tqdm.tqdm(asyncio.as_completed(tasks), total=len(tasks)):
            responses.append(await f)
    return responses

number = 20#000
loop = asyncio.get_event_loop()
loop.run_until_complete(run(number))
