"""
正则匹配练习
1．匹配一个.com邮箱格式字符串
2．匹配一个密码8-12位数字字母下划线构成
3．匹配一个数字正数﹐负数﹐整数﹐小数﹐分数1/2，百分数45%
4．匹配一段文字中以大写字母开头的单词﹐注意文字中可能有例如：iPython(不算) H-base（算)
单词可能有大写字母小写字母- _
"""
import re

# 1．匹配一个.com邮箱格式字符串
s = '我的邮箱是: shikybird@qq.com  995587@qq.com'
print(re.findall(r'\w+@\w+\.com', s))

# 标准邮箱正则表达式
print(re.findall(r'\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b', s))

# 2．匹配一个密码8-12位数字字母下划线构成
s = '我的密码是： abc_231_b'
print(re.findall(r'\w{8,12}', s))

# 3．匹配一个数字正数﹐负数﹐整数﹐小数﹐分数1/2，百分数45%
s = '2 -123 23.5 -234.543 3/4 45% -45.4% -(1/2) 1/3'
print(re.findall(r'[- (]*\d+[/.%)\d]*', s))

# 4．匹配一段文字中以大写字母开头的单词﹐注意文字中可能有例如：
# iPython(不算) H-base（算)
# 单词可能有大写字母小写字母- _
s = """
To  H-base iPython Jupyter-Notebook IPython I-Python BSD I_python 
"""
print(re.findall(r'\b[A-Z][a-zA-Z-_]*', s))
 