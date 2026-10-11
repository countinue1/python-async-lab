import asyncio
import time
import httpx

async def 问模型(问题):
    async with httpx.AsyncClient(timeout=120) as client:
        resp = await client.post(
            "http://localhost:11434/v1/chat/completions",
            json={
                "model": "qwen2.5:7b",
                "messages": [{"role": "user", "content": 问题}],
                "max_tokens": 50,  # 回答别太长，省时间
            },
        )
        data = resp.json()
        return data["choices"][0]["message"]["content"]

async def main():
    问题 = ["用一句话介绍 Python", "用一句话介绍异步编程", "1+1 等于几"]
    开始 = time.time()
    答案 = await asyncio.gather(*(问模型(q) for q in 问题))
    print(f"总耗时: {time.time() - 开始:.1f} 秒\n")
    for q, a in zip(问题, 答案):
        print(f"问: {q}\n答: {a}\n")

asyncio.run(main())
