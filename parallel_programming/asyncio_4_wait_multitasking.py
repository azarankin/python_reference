
import asyncio
import time



async def do_work(delay: int, item: str):
    print(f'{delay + 1}item: {item} start')
    await asyncio.sleep(delay + 1)
    print(f'{delay + 1}item: {item} done')



todo = ['get package', 'laundry', 'back cake']

async def main():
    start = time.perf_counter()
    #one by one:
    #for i, item in enumerate(todo):
    #    await do_work(i, item)

    tasks = [asyncio.create_task(do_work(i, item)) for i, item in enumerate(todo)]
    #done, pending = await asyncio.wait(tasks)
    result = await asyncio.gather(*tasks, return_exceptions=True)

    #async with asyncio.TaskGroup() as tg:  # python 3.11
    #    tasks = [tg.create_task(do_work(i ,item)) for i, item in enumerate(todo)]


    end = time.perf_counter()
    print(f'it took: {end - start:.2f}s')

if __name__ == '__main__':
    asyncio.run(main())


