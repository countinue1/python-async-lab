import asyncio
import json
import httpx

async def 问模型(问题):
    try:
        async with httpx.AsyncClient(timeout=120) as client:
            resp = await client.post(
                "http://localhost:11434/v1/chat/completions",
                json={
                    "model": "qwen2.5:7b",
                    "messages": [{"role": "user", "content": 问题}],
                    "max_tokens": 50,
                },
            )
            data = resp.json()
            return {"问题": 问题, "回答": data["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"问题": 问题, "回答": f"出错了: {e}"}

async def main():
    问题 = ["用一句话介绍 Python", "用一句话介绍 JSON", "用一句话介绍异常处理"]
    结果 = await asyncio.gather(*(问模型(q) for q in 问题))

    with open("问答记录.json", "w", encoding="utf-8") as f:
        json.dump(结果, f, ensure_ascii=False, indent=2)
    print("已保存到 问答记录.json，共", len(结果), "条")

asyncio.run(main())
