"""
    flags.py
    flags 扩展功能演示
"""

import re

s = """Hello 
北京
"""

# 只能匹配ASCII编码
regex = re.compile(r'\w+', flags=re.A)
l = regex.findall(s)
print(l)

# 不区分大小写
regex = re.compile(r'[a-z]+', flags=re.I)
l = regex.findall(s)
print(l)

# .可以匹配换行（即.可以代表任意字符）
regex = re.compile(r'.+', flags=re.S)
l = regex.findall(s)
print(l)

# ^,$ 匹配每一行开头结尾位置
regex = re.compile(r'^北京', flags=re.M)
l = regex.findall(s)
print(l)

# 给正则分行注释
pattern = r"""\w+ # 匹配hello
\s+ # 匹配换行
\w+ # 匹配北京
"""
regex = re.compile(pattern, flags=re.X)
l = regex.findall(s)
print(l)

# 既给正则加注释，又忽略大小写
regex = re.compile(pattern, flags=re.X | re.I)
l = regex.findall(s)
print(l)
