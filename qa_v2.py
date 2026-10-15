import asyncio
import httpx
import json
import time


sem =asyncio.Semaphore(3)
完成数 = 0

async def 问一次(问题):
    #最内层：只管发一次请求的事情
    async with httpx.AsyncClient(timeout = 120) as client:
        resp = await client.post(
            "http://localhost:11434/v1/chat/completions",
            json={"model":"qwen2.5:7b",
            "messages":[{"role":"user","content":问题}],
            "max_tokens":50
            },
        )
        return resp.json()["choices"][0]["message"]["content"]

async def 问模型(问题, sem):
    global 完成数
    #中层：限流 + 重试 +异常隔离
    async with sem:
        回答 = "3次都失败了，放弃"
        for 第几次 in range(3):
            try:
                回答 = await asyncio.wait_for(问一次(问题), timeout=60)
            except (TimeoutError, httpx.HTTPError) as e:
                print(f"第{第几次+1}次失败: {e},重试...")
        完成数 += 1
        print(f"进度：{完成数}/10")
        return {"问题": 问题, "回答": 回答}

async def main():
    问题 = ["什么是机器学习中的“过拟合”（Overfitting）现象？",
            "在Python编程语言中，列表（List）和元组（Tuple）最核心的区别是什么？",
            "著名的“图灵测试”主要用来评估什么？",
            "逻辑推理：池塘里的睡莲面积每天增加一倍，30天刚好长满整个池塘。请问第几天时长满半个池塘？",
            "逻辑推理：你有两根粗细不均的香，每根完全烧完都需要正好1小时。你如何用这两根香测出准确的45分钟？",
            "数学计算：一个水池有进水管和出水管。单开进水管3小时蓄满，单开出水管4小时放空水池。两管齐开，需要多少小时能注满水池？",
            "概念解释：大语言模型（LLM）在生成内容时出现的“幻觉”（Hallucination）指的是什么？",
            "地理常识：地球表面占据面积最大的大洋是哪一个？",
            "物理常识：光在真空中传播的速度大约是每秒多少公里？",
            "历史常识：世界上第一位进入太空的宇航员是谁？"
            ]
    开始 = time.time()
    结果 = await asyncio.gather(*(问模型(q, sem) for q in 问题))
    print(f"总耗时：{time.time() - 开始:.1f} 秒")
    with open("问答记录-v2.json", "w", encoding="utf-8") as f:
        json.dump(结果, f, ensure_ascii=False, indent=2)
    print(f"已保存 {len(结果)} 条到 问答记录-v2.json")


asyncio.run(main())



        