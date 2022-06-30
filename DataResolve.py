import re

'''正则表达式'''
# print(re.match('com','www.baidu.com').group())
# print(re.search('com','www.baidu.com').group())
# phone = "2004-959-559 # 这是一个电话号"
#
# num = re.sub(r'\D',"",phone)
# print(num)

# str = "<div class=\"jay\">周杰伦</div>\n<div class=\"jj\">林俊杰</div>"
#
# pattern = "<div class=\".*?\">.*?</div>"
#
# result = re.findall(pattern,str)
# # 如果findall 匹配的正则表达式中含分组
# # 那么最终的返回值将是一个由分组元组组成的列表
# # 即一次匹配成功的结果是一个元组，其中包含多个分组
# # 而最终的列表中可能有多次匹配成功的结果，即多个元组
# print(result)  # 这样就能只获得人名
#
# result1 = re.finditer(pattern,str)
#
# pat = re.compile(pattern)
# print(pat)
# print(next(pat.finditer(str)))


# for i in result1:
#     print(i.group())

'''稍作修改'''
'''可以提取指定内容'''
# pattern = "<div class=\"(.*?)\">(.*?)</div>" # 给两个.*?加上括号
#
# result = re.findall(pattern,str)
# # 如果findall 匹配的正则表达式中含分组
# # 那么最终的返回值将是一个由分组元组组成的列表
# # 即一次匹配成功的结果是一个元组，其中包含多个分组
# # 而最终的列表中可能有多次匹配成功的结果，即多个元组
# print(result[0][1])  # 这样就能只获得人名
#
# result1 = re.finditer(pattern,str)
#
# for i in result1:
#     print(i.group())

# split = re.split('\W',str)  # split 方法是返回去掉正则表达式后的列表
# print(split)

'''提取指定内容的方法'''
str = """
<div class='jay'><span id='1'>机器人</span></div>
<div class='jj'><span id='2'>人工智能</span></div>
<div class='jolin'><span id='3'>区块链技术</span></div>
<div class='sylar'><span id='4'>数据库</span></div>
<div class='tory'><span id='5'>深度学习</span></div>
"""

pattern = r"<div class='(?P<class>.*?)'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>"

obj = re.compile(pattern)

result = obj.finditer(str)

for data in result:
    print(data.group("class"))
    print(data.group("id"))
    print(data.group("name"))

