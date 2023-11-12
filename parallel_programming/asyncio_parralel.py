import asyncio
import time


#run

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(f"{what} (delay {delay}s)")

async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


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



