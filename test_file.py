import json

记录 = {"日期": "2026-10-11", "学了": "异常处理+JSON"}

with open("学习记录.json", "w", encoding="utf-8") as f:
    json.dump(记录, f, ensure_ascii=False, indent=2)  # 直接写进文件

with open("学习记录.json", "r", encoding="utf-8") as f:
    读回来 = json.load(f)  # 直接从文件读成字典
print(读回来["学了"])
