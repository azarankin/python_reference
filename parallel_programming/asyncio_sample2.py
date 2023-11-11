import asyncio
import aiohttp
import time



async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main3():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')

    # Fetch a URL asynchronously
    url = 'https://www.example.com'
    content = await fetch_url(url)
    print(f"Fetched content from {url}: {content}")

    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main3())