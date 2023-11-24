import asyncio
import time


#asyncio.gather
async def my_async_function():
    
    await asyncio.sleep(2)
    print("^^^^^^ 2s delay")
async def my_async_function2():
    await asyncio.sleep(1)
    print("------ 1s delay")

async def main2():
    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(my_async_function2())
    task2 = asyncio.create_task(my_async_function())
    await asyncio.gather(task1, task2)
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main2())

