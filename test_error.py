try:
    数字 = int("123")
    print(f"转换成功: {数字}")
except ValueError:
    print("抓到了！转不成数字")
else:
    print("没有出错，else 跑了")
