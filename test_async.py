import asyncio
import time

async def 任务(名字, 秒数):
    print(f"{名字} 开始")
    await asyncio.sleep(秒数)
    print(f"{名字} 结束")

async def main():
    开始 = time.time()
    await asyncio.gather(
        任务("A", 1),
        任务("B", 2),
        任务("C", 3),
    )
    print(f"总耗时: {time.time() - 开始:.1f} 秒")

asyncio.run(main())
