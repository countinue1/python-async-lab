import asyncio
import time


sem = asyncio.Semaphore(2)

async def task(name):
    async with sem:
        print(f'{name} 进门')
        await asyncio.sleep(2)
        print(f'{name} 出门')

async def main():
    开始 =time.time()
    await asyncio.gather(*(task(f'T{i}') for i in range(5)))
    print(f'总耗时： {time.time() - 开始:.1f}秒')


asyncio.run(main())            