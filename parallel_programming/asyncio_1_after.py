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



