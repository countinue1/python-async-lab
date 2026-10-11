import json

# 1. 字典转文本
我 = {"name": "追梦人", "目标": "大模型应用开发", "周数": 36}
文本 = json.dumps(我, ensure_ascii=False, indent=2)
print(文本)

# 2. 文本转回字典
回来 = json.loads(文本)
print(f"\n目标是: {回来['目标']}")

# 3. 试试把 ensure_ascii=False 去掉，看中文变成什么样
