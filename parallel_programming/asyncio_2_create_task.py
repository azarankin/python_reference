import asyncio
import time



#asyncio.create_task

async def async_func1():
    return 42

async def async_func2():
    return 79

async def main3():
    await asyncio.gather(async_func1(), async_func2())
    await asyncio.sleep(1)
    task = asyncio.create_task(async_func1())
    await task
    
asyncio.run(main3())


