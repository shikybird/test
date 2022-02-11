"""
    regex.py re模块 功能函数演示
"""

import re

# 目标字符串
s = "Alex:1994, Sunny:1996"
pattern = r'(\w+):(\d+)'  # 正则表达式

# re 模块调用findall    *****
l = re.findall(pattern, s)
print(l)

# compile 对象调用findall  *****
regex = re.compile(pattern)
l = regex.findall(s, 0, 12)
print(l)

# 按照正则表达式匹配内容切割字符串
l = re.split(r'[:,]', s)
print(l)

# 替换目标字符串
s1 = re.sub(r':', '-', s)
s2 = re.sub(r':', '-', s, 1)
s3 = re.subn(r':', '-', s)  # 返回值里显示替换次数
print(s1)
print(s2)
print(s3)
